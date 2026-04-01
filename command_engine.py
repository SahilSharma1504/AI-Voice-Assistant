import webbrowser
import pywhatkit
import wikipedia
import pyjokes
import pyautogui
import os
import datetime


def process_command(command):
    """
    Process system commands for the assistant.
    Returns response if command matched.
    Returns None if command not found.
    """

    if command == "":
        return "I didn't hear anything."

    # Greeting
    if "hello" in command:
        return "Hello, how can I help you?"

    # Time
    if "time" in command:
        return datetime.datetime.now().strftime("Current time is %H:%M")

    # Date
    if "date" in command:
        return datetime.datetime.now().strftime("Today is %d %B %Y")

    # Open Google
    if "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    # Open YouTube
    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    # Play YouTube song
    if "play" in command:
        song = command.replace("play", "")
        pywhatkit.playonyt(song)
        return "Playing " + song

    # Wikipedia search
    if "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        try:
            return wikipedia.summary(topic, sentences=2)
        except:
            return "Wikipedia search failed."

    # Tell joke
    if "joke" in command:
        return pyjokes.get_joke()

    # Screenshot
    if "screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        return "Screenshot saved."

    # Open Notepad
    if "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    # Volume controls
    if "volume up" in command:
        pyautogui.press("volumeup")
        return "Volume increased"

    if "volume down" in command:
        pyautogui.press("volumedown")
        return "Volume decreased"

    # Shutdown computer
    if "shutdown computer" in command:
        os.system("shutdown /s /t 1")
        return "Shutting down the computer"

    return None