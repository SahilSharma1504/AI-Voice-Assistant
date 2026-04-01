import os
import pyautogui


def open_notepad():
    """
    Open Windows Notepad
    """
    os.system("notepad")
    return "Opening Notepad"


def shutdown_computer():
    """
    Shutdown the computer
    """
    os.system("shutdown /s /t 1")
    return "Shutting down the computer"


def restart_computer():
    """
    Restart the computer
    """
    os.system("shutdown /r /t 1")
    return "Restarting the computer"


def lock_computer():
    """
    Lock the computer screen
    """
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "Locking the computer"


def volume_up():
    """
    Increase system volume
    """
    pyautogui.press("volumeup")
    return "Volume increased"


def volume_down():
    """
    Decrease system volume
    """
    pyautogui.press("volumedown")
    return "Volume decreased"


def mute_volume():
    """
    Mute system volume
    """
    pyautogui.press("volumemute")
    return "Volume muted"


def take_screenshot():
    """
    Take screenshot and save it
    """
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    return "Screenshot saved"