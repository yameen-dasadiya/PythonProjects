lst = [1, 2, 3, 4, 5, 6, 8, 5, 5, 5, 0, 7]
dup = []
for i in lst:
    if i not in dup:
        dup.append(i)
print(dup)