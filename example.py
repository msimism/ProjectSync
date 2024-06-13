import datetime
import re

name = input("Enter your name: ").strip()

pattern = r'\b[A-Za-z]+\b'

names = re.findall(pattern, name)

current_hour = datetime.datetime.now().hour

if current_hour < 12:
    greeting = "Good morning"
elif current_hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

names_list = ', '.join(names)
print(f"{greeting}, {names_list}!")
