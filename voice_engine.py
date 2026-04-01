import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Configure voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# Optional: adjust speaking speed
engine.setProperty("rate", 180)


def speak(text):
    """
    Convert text to speech.
    """
    if not text:
        return

    engine.say(text)
    engine.runAndWait()


def listen():
    """
    Capture voice from microphone and convert it to text.
    """

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)
        command = command.lower()

        print("User said:", command)

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""

    return command


def test_voice():
    """
    Simple test function for voice engine.
    """

    speak("Voice engine is working.")

    command = listen()

    if command:
        speak("You said " + command)
    else:
        speak("I did not hear anything.")