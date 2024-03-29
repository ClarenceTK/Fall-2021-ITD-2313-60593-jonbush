from typing import Callable, Dict, List, Tuple, Union

from uaclient.entitlements import repo

CC_README = "/usr/share/doc/ubuntu-commoncriteria/README"


class CommonCriteriaEntitlement(repo.RepoEntitlement):

    help_doc_url = "https://ubuntu.com/cc-eal"
    name = "cc-eal"
    title = "CC EAL2"
    description = "Common Criteria EAL2 Provisioning Packages"
    repo_key_file = "ubuntu-cc-keyring.gpg"
    is_beta = True

    @property
    def messaging(self) -> Dict[str, List[Union[str, Tuple[Callable, Dict]]]]:
        return {
            "pre_install": [
                "(This will download more than 500MB of packages, so may take"
                " some time.)"
            ],
            "post_enable": [
                "Please follow instructions in {} to configure EAL2".format(
                    CC_README
                )
            ],
        }
