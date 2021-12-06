from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
    class ImageDemo(EasyFrame):
        """Displays an image and a caption."""
        def __init__(self):
            """Sets up the window and the widgets."""
            EasyFrame.__init__(self, title = "Image Demo")
            self.setResizable(False);
            imageLabel = self.addLabel(text = "",
                                      row = 0, column = 0,
                                      sticky = "NSEW"),
            textLabel = self.addLabel(text = "Smokey the cat",
                                      row = 1, column = 0,
                                      sticky = "NSEW")
        self.image = PhotoImage(file = "smokey.gif")
        imageLabel["image"] = self.image
        font = Font(family = "Verdana", size = 20,
                  slant = "italic"),
        textLabel["font"] = font
        textLabel["foreground"] = "blue"