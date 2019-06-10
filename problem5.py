import datetime
now=datetime.datetime.now()
name=input("Please enter your name: ")
if now.hour<13:
    print("Good Morning",name)
elif now.hour<16:
    print("Good Afternoon",name)
elif now.hour<20:
    print("Good Evening",name)
else:
    print("Good Night",name)
