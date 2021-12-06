from breezypythongui import EasyFrame
def computeDistance(height, index, bounces):
    distance = 0.0
    height = self.heightField.getNumber()
    ratio = self.indexField.getNumber()
    numBounces = self.bouncesField.getNumber()
    for bounce in range(numBounces):
        bounceHeight = height * ratio
        distance += height + bounceHeight
        height = bounceHeight
    self.distanceField.setNumber(distance)
class BouncyGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Bouncy")
        self.addLabel(text="Initial Height",
                        row=0, column=0)
        self.heightField = self.addFloatField(value=0.0,
                        row=0, column=1)
        self.addLabel(text="Bounciness Index",
                        row=1, column=0)
        self.indexField = self.addFloatField(value=0.0,
                        row=1, column=1)
        self.addLabel(text="Number of bounces",
                        row=2, column=0)
        self.bouncesField = self.addIntegerField(value=0,
                        row=2, column=1)
        self.addButton(text="Compute distance",
                        row=3, column=0, columnspan=2,
                        command=self.computeDistance)
        self.addLabel(text="Distance traveled",
                        row=4, column=0)
        self.distanceField = self.addFloatField(value=0,
                        row=4, column=1)
    def computeDistance(self):
        distance = 0.0
        height = self.heightField.getNumber()
        ratio = self.indexField.getNumber()
        numBounces = self.bouncesField.getNumber()
        for bounce in range(numBounces):
            bounceHeight = height * ratio
            distance += height + bounceHeight
            height = bounceHeight
        self.distanceField.setNumber(distance)

def main():
    BouncyGUI().mainloop()

if __name__ == "__main__":
    main()