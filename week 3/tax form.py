TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0 #declaring required varaibles

grossIncome = float(input("Enter the gross income: ")) #asking user to enter gross income
numDependents = int(input("Enter the number of dependents: ")) #asking user to enter depenedents
#calculating taxableIncome
taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * numDependents)
#calculating incomeTax
incomeTax=taxableIncome * TAX_RATE
print("The income tax is $" + str(round(incomeTax,2))) 