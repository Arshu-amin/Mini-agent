import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

def get_greeting():
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

name = input("Enter your name: ")
greeting = get_greeting()

message = f"{greeting}, {name}! Welcome."

print(message)

engine.say(message)
engine.runAndWait()