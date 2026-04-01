from voice_engine import speak, listen
from ai_engine import ask_ai

import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import pyautogui
import os


def process(command):

    command = command.lower()

    if command == "":
        return "I didn't hear anything."

    elif "hello" in command:
        return "Hello, how can I help you?"

    elif "time" in command:
        return datetime.datetime.now().strftime("Current time is %H:%M")

    elif "date" in command:
        return datetime.datetime.now().strftime("Today is %d %B %Y")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open chrome" in command:
        try:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        except:
            webbrowser.open("https://google.com")
        return "Opening Chrome"

    elif "play" in command:
        song = command.replace("play", "")
        pywhatkit.playonyt(song)
        return "Playing " + song

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        try:
            return wikipedia.summary(topic, sentences=2)
        except:
            return "Wikipedia search failed."

    elif "joke" in command:
        return pyjokes.get_joke()

    elif "screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        return "Screenshot saved."

    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    elif "volume up" in command:
        pyautogui.press("volumeup")
        return "Volume increased"

    elif "volume down" in command:
        pyautogui.press("volumedown")
        return "Volume decreased"

    elif "shutdown computer" in command:
        os.system("shutdown /s /t 1")
        return "Shutting down the computer"

    elif "exit" in command:
        return "exit"

    else:
        return ask_ai(command)