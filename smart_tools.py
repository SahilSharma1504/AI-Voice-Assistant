import requests
import datetime


def calculate(expression):
    try:
        result = eval(expression)
        return f"The result is {result}"
    except:
        return "I could not calculate that."


def get_weather(city="London"):

    try:

        url = f"https://wttr.in/{city}?format=3"
        weather = requests.get(url).text

        return weather

    except:
        return "Weather service not available."


def internet_search(query):

    return f"You can search this on the internet: {query}"


def create_reminder(text):

    time = datetime.datetime.now().strftime("%H:%M")

    return f"Reminder saved: {text} at {time}"