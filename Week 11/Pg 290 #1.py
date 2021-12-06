TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

from breezypythongui import EasyFrame


class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Tax Calculator")

        self.addLabel(text="Income", row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(value=0, row=1, column=1)

        self.addButton(text="Compute", row=2, column=0, columnspan=2, command=self.computeTax)

        self.addLabel(text="Total tax", row=3, column=0)
        self.taxField = self.addFloatField(value=0.0, row=3, column=1, precision=2)

    def computeTax(self):
        """Obtains the data from the input fields and uses
        them to compute the tax, which is sent to the
        output field."""
        income = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        tax = (income - STANDARD_DEDUCTION - numDependents*DEPENDENT_DEDUCTION) * TAX_RATE
        self.taxField.setNumber(tax)

def main():
    TaxCalculator().mainloop()

if __name__ == '__main__':
    main()