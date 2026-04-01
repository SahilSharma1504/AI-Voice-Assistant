import json
import os

SETTINGS_FILE = "assistant_settings.json"


default_settings = {
    "assistant_name": "Nova",
    "theme": "dark",
    "voice_rate": 180,
    "voice_id": 0,
    "mic_enabled": True
}


def load_settings():
    """
    Load settings from file
    """

    if not os.path.exists(SETTINGS_FILE):
        save_settings(default_settings)
        return default_settings

    try:
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)
            return settings
    except:
        return default_settings


def save_settings(settings):
    """
    Save settings to file
    """

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)


def get_setting(key):
    """
    Get a specific setting
    """

    settings = load_settings()
    return settings.get(key)


def update_setting(key, value):
    """
    Update a specific setting
    """

    settings = load_settings()
    settings[key] = value
    save_settings(settings)


def reset_settings():
    """
    Reset settings to default
    """

    save_settings(default_settings)