import datetime

name = input("Enter your name: ")
current_hour = datetime.datetime.now().hour

if current_hour < 12:
    greeting = "Good morning"
elif current_hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print(f"{greeting}, {name}!")
