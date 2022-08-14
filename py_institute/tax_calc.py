income = float(input("Enter the annual income: "))
if income<85528.0 :
    tax=((income*(18/100))-556.2)
else :
    tax=(14839.2 + ((income-85528.0)*(32/100)))
tax = round(tax, 0)
if tax<0 : print("The tax is:", 0.0 , "thalers")
else : print("The tax is:", tax, "thalers")
