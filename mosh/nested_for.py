#for x in range(4):
  #  for y in range(6):
     #   print((x+1) * "*" , (y+1)* "*", sep="")

num = [5,2,5,2,2]

for i in num:
    op = ""
    for j in range(i):
        op += "X "
    print(op)