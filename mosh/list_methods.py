lst = [1, 2, 3, 4, 5, 6, 8, 5, 5, 5, 0, 7]
lst.append(20)  # add values at last
print(lst)
lst.insert(1, 10)  # insert values at given position
print(lst)
lst.remove(3)
print(lst)
lst.pop(-1)
print(lst)
print(lst.index(5))
print(4 in lst)
print(50 in lst)
print(lst.count(5))
lst.sort()
print(lst)
lst.reverse()
print(lst)
lst2 = lst.copy()
print(lst2)
lst.clear()
print(lst)
