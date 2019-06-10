import datetime
now=datetime.datetime.now()
age=int(input("Enter your age: "))
print("The year you turn 95 is ",(95-age+now.year))
