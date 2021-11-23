#
#  Copyright (c) 2019 Canonical
#
#  Authors:
#       Andrea Azzarone <andrea.azzarone@canonical.com>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
#  USA

from gettext import gettext as _
from contextlib import closing
from urllib.parse import urlencode
import http.client
import logging
import json
import socket

import gi
from gi.repository import Gio, GLib, GObject

try:
    import dateutil.parser

    gi.require_version('Snapd', '1')
    from gi.repository import Snapd
except(ImportError, ValueError):
    pass

from softwareproperties.gtk.utils import (
    has_gnome_online_accounts,
    is_current_distro_lts,
    is_current_distro_supported,
    retry
)

from softwareproperties.LivepatchSnap import LivepatchSnap

def datetime_parser(json_dict):
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = dateutil.parser.parse(value)
        except (ValueError, TypeError):
            pass
    return json_dict

class LivepatchAvailability:
    FALSE = 0
    TRUE = 1
    NO_CONNECTIVITY=3
    CHECKING = 2


# copied from update-manager package UpdateManager/Core/LivePatchSocket.py
class UHTTPConnection(http.client.HTTPConnection):

    def __init__(self, path):
        http.client.HTTPConnection.__init__(self, 'localhost')
        self.path = path

    def connect(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(self.path)
        self.sock = sock


# Constants
LIVEPATCH_SNAP_CURRENT_DIR = '/var/snap/canonical-livepatch/current'
LIVEPATCH_SOCKET = f'{LIVEPATCH_SNAP_CURRENT_DIR}/livepatchd.sock'
LIVEPATCH_PRIV_SOCKET = f'{LIVEPATCH_SNAP_CURRENT_DIR}/livepatchd-priv.sock'
LIVEPATCH_RUNNING_FILE = '/var/snap/canonical-livepatch/common/machine-token'


class LivepatchService(GObject.GObject):

    ENABLE_ERROR_MSG = _('Failed to enable Livepatch: {}')
    DISABLE_ERROR_MSG = _('Failed to disable Livepatch: {}')

    # GObject.GObject
    __gproperties__ = {
        'availability': (
            int, None, None,
            LivepatchAvailability.FALSE,
            LivepatchAvailability.CHECKING,
            LivepatchAvailability.FALSE,
            GObject.ParamFlags.READABLE),
        'availability-message': (
            str, None, None, None, GObject.ParamFlags.READABLE),
        'enabled': (
            bool, None, None, False, GObject.ParamFlags.READABLE),
    }

    def __init__(self):
        GObject.GObject.__init__(self)

        self._timeout_id = 0

        self._snap = LivepatchSnap()

        # Init Properties
        self._availability = LivepatchAvailability.FALSE
        self._availability_message = None
        lp_file = Gio.File.new_for_path(path=LIVEPATCH_RUNNING_FILE)
        self._enabled = lp_file.query_exists()

        # Monitor connectivity status
        self._nm = Gio.NetworkMonitor.get_default()
        self._nm.connect('notify::connectivity', self._network_changed_cb)

        # Monitor status of canonical-livepatch
        self._lp_monitor = lp_file.monitor_file(Gio.FileMonitorFlags.NONE)
        self._lp_monitor.connect('changed', self._livepatch_enabled_changed_cb)

    def do_get_property(self, pspec):
        if pspec.name == 'availability':
            return self._availability
        elif pspec.name == 'availability-message':
            return self._availability_message
        elif pspec.name == 'enabled':
            return self._enabled
        else:
            raise AssertionError

    # Public API
    def trigger_availability_check(self):
        """Trigger a Livepatch availability check to be executed after a short
        timeout. Multiple triggers will result in a single request.

        A notify::availability will be emitted when the check starts, and
        another one when the check ends.
        """
        def _update_availability():
            # each rule is a tuple of two elements, a callable and a string. The
            # string rapresents the error message that needs to be shown if the
            # callable returns false.
            rules = [
                (lambda: self._snap.get_status() != Snapd.SnapStatus.UNKNOWN,
                    _('Canonical Livepatch snap is not available.')),
                (has_gnome_online_accounts,
                    _('Gnome Online Accounts is required to enable Livepatch.')),
                (is_current_distro_lts,
                    _('Livepatch is not available for this release.')),
                (is_current_distro_supported,
                    _('The current release is no longer supported.'))]

            if self._nm.props.connectivity != Gio.NetworkConnectivity.FULL:
                self._availability = LivepatchAvailability.NO_CONNECTIVITY
                self._availability_message = None
            else:
                for func, message in rules:
                    if not func():
                        self._availability = LivepatchAvailability.FALSE
                        self._availability_message = message
                        break
                else:
                    self._availability = LivepatchAvailability.TRUE
                    self._availability_message = None

            self.notify('availability')
            self.notify('availability-message')

            self._timeout_id = 0
            return False

        self._availability = LivepatchAvailability.CHECKING
        self._availability_message = None
        self.notify('availability')
        self.notify('availability-message')

        if self._timeout_id == 0:
            self._timeout_id = GLib.timeout_add_seconds(3, _update_availability)

    def set_enabled(self, enabled, token):
        """Enable or disable Canonical Livepatch in the current system. This
        function will return once the operation succeeded or failed.

        Args:
            enabled(bool): wheater to enable or disable the service.
            token(str): the authentication token to be used to enable Canonical
                Livepatch service.

        Returns:
            (False, '') if successful, (True, error_message) otherwise.
        """
        if self._enabled == enabled:
            return False, ''

        if not enabled:
            return self._disable_service()
        elif self._snap.get_status() == Snapd.SnapStatus.ACTIVE:
            return self._enable_service(token)
        else:
            success, msg = self._snap.enable_or_install()
            return self._enable_service(token) if success else (True, msg)

    def get_status(self):
        """Synchronously retrieve the status of Canonical Livepatch.

        Returns:
            str: The status. A valid string for success, None otherwise.
        """
        try:
            params = {'verbosity': 3, 'format': 'json'}
            with closing(UHTTPConnection(LIVEPATCH_SOCKET)) as c:
                url = f'/status?{urlencode(params)}'
                c.request('GET', url)
                response = c.getresponse()
                return json.loads(response.read(), object_hook=datetime_parser)
        except Exception as e:
            logging.debug('Failed to get Livepatch status: {}'.format(str(e)))
            return None

    # Private methods
    def _enable_service(self, token):
        """Enable Canonical Livepatch in the current system. This function will
        return once the operation succeeded or failed.

        Args:
            token(str): the authentication token to be used to enable Canonical
                Livepatch service.

        Returns:
            (False, '') if successful, (True, error_message) otherwise.
        """
        try:
            return self._enable_service_with_retry(token)
        except Exception as e:
            return True, self.ENABLE_ERROR_MSG.format(str(e))

    @retry(Exception)
    def _enable_service_with_retry(self, token):
        params = {'auth-token': token}
        with closing(UHTTPConnection(LIVEPATCH_PRIV_SOCKET)) as c:
            url = f'/enable?{urlencode(params)}'
            c.request('PUT', url)
            response = c.getresponse()
            if 400 <= response.status < 600:
                return True, self.ENABLE_ERROR_MSG.format(response.read().decode('utf-8'))
        return False, ''

    def _disable_service(self):
        """Disable Canonical Livepatch in the current system. This function will
        return once the operation succeeded or failed.

        Returns:
            (False, '') if successful, (True, error_message) otherwise.
        """
        try:
            return self._disable_service_with_retry()
        except Exception as e:
            return True, self.DISABLE_ERROR_MSG.format(str(e))


    @retry(Exception)
    def _disable_service_with_retry(self):
        with closing(UHTTPConnection(LIVEPATCH_PRIV_SOCKET)) as c:
            c.request('PUT', '/disable')
            response = c.getresponse()
            if 400 <= response.status < 600:
                return True, self.DISABLE_ERROR_MSG.format(response.read().decode('utf-8'))
        return False, ''

    # Signals handlers
    def _network_changed_cb(self, monitor, network_available):
        self.trigger_availability_check()

    def _livepatch_enabled_changed_cb(self, fm, file, other_file, event_type):
        enabled = file.query_exists()
        if self._enabled != enabled:
            self._enabled = enabled
            self.notify('enabled')
