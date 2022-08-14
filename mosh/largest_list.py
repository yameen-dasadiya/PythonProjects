lst = [2,4,3,1,7,9,8,6,5,10]
print (lst)
largest = lst[0]
for i in range(len(lst)):
    if largest < lst[i]:
        largest = lst[i]
print("largest number is: ", largest)


