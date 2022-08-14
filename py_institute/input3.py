hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hours = (hour + (mins+dura)//60)%24
minutes = (mins+dura)%60
print(hours, ":",minutes)
