def diplay_bo(bo):
    print("+-------"*3,"+", sep="")
    for row in range (3):
        print ("|       "*3, "|", sep="")
        for col in range (3):
            print("|   " + str (bo[row][col]+"   ", end=""))
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")
