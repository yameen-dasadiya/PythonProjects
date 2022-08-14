def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)


#parameter & argument passing.
def intro1(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

intro1("Skywalker", "Luke")
intro1("Quick", "Jesse")
intro1("Kent", "Clark")

def intro2(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

intro2("James", "Doe")
intro2("Henry")
intro2(first_name="William")

def intro3(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

intro3()
intro3(last_name="Hopkins")
