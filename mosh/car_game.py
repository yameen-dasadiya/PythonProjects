command = ""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started...")
        else:
            print("Car started...")
            started = True
    elif command == "stop":
        if stopped:
            print("Car already stopped...")
        else:
            print("Car has been stopped...")
            stopped = True
    elif command == "help":
        print("""
    start - to start car
    stop - to stop car
    quit - to quit 
        """)
    elif command == "quit":
        break
    else:
        print("Please Enter Proper command.")
