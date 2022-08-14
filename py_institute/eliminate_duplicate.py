
#method1
my_list = [1,2,2,3,1,4,5,1,2,6]
new_list = []
for i in (my_list):
    if i not in new_list:
        new_list.append(i)
print(list(new_list))


#method2
my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
print("List Before ", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list

print("List After removing duplicates ", my_list)
