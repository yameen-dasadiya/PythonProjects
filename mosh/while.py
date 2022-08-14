sn = 9
guess = 0
while guess < 3:
    num = int(input("Enter number:"))
    guess+=1
    if num == sn:
        print("Ypieee ! That's Secret Number")
        break
else:
    print("Sorry you are wrong.")

