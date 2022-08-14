income = True
credit = True

if income and credit:
    print("Eligible for Loan")
if not (income or credit):
    print("Not eligible for loan")
