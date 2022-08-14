wt = int(input("Enter Weight: "))
unit= input("(G)m or (K)g: ")
if unit.upper() == "G":
    kg = wt/1000
    print(kg, "Kilograms")
elif unit.upper() == "K":
    gm = wt*1000
    print(gm , "Grams")
else:
    print("Enter valid unit.")