# step 1
beatles=[]
print("Step 1:", beatles)

# step 2
beatles.append("Jhon lennon")
beatles.append("Paul McCar")
beatles.append("George Hari")
print("Step 2:", beatles)

# step 3
beatles.append(input(" Enter Remaining members: "))
print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-2]
print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
