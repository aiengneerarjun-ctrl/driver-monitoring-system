from playsound import playsound
import threading
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ALERT_SOUND = os.path.join(
    BASE_DIR,
    "assets",
    "alert.mp3"
)

def play_alert_sound():
    playsound(ALERT_SOUND)

def trigger_alert():
    threading.Thread(
        target=play_alert_sound,
        daemon=True
    ).start()