class ButtonDemo(EasyFrame):
    """Illustrates command buttons and user events."""
    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self)
        self.label = self.addLabel(text = "Hello world!",
                                    row = 0, column = 0,
                                    columnspan = 2,
                                    sticky = "NSEW")
        self.clearBtn = self.addButton(text = "Clear",
                                        row = 1, column = 0)
        self.restoreBtn = self.addButton(text = "Restore",
                                        row = 1, column = 1,
                                        state = "disabled")
class ButtonDemo(EasyFrame):
    """Illustrates command buttons and user events."""
    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self)
        self.label = self.addLabel(text = "Hello world!",
                                    row = 0, column = 0,
                                    columnspan = 2,
                                    sticky = "NSEW")
        self.clearBtn = self.addButton(text = "Clear",
                                    row = 1, column = 0,
                                    command = self.clear)
        self.restoreBtn = self.addButton(text = "Restore",
                                    row = 1, column = 1,
                                    state = "disabled",
                                    command = self.restore)
    def clear(self):
        """Resets the label to the empty string and updates the button states."""
        self.label["text"] = ""
        self.clearBtn["state"] = "disabled"
        self.restoreBtn["state"] = "normal"
    def restore(self):
        """Resets the label to 'Hello world!' and updates the button states.""" 
        self.label["text"] = "Hello world!"
        self.clearBtn["state"] = "normal"
        self.restoreBtn["state"] = "disabled"