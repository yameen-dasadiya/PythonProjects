def name_fun():
    name = input("Enter your name: ")
    len_name = len(name)
    if len_name >= 50:
        print("Name is too long.")
    elif len_name <= 3:
        print("Name is too short.")
    elif 3 <= len_name <= 50:
        print("Name looks good.")
    return name


n = name_fun()
print("your name: ", n)
print("Enter your name again:" , name_fun())