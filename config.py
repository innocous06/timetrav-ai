import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
APP_NAME = "TimeTraveler AI"
APP_SUBTITLE = "Where History Speaks Through Those Who Made It"
DEFAULT_VOICE_LANG = "en"
VOICE_SLOW = False
MAX_IMAGE_SIZE = (1024, 1024)
WIKIPEDIA_IMAGE_COUNT = 5
GEMINI_MODEL = "gemini-2.0-flash"

FALLBACK_PERSONA = {
    "name": "Ancient Historian",
    "title": "Keeper of History",
    "era": "Timeless",
    "avatar": "📜",
    "connection": "I have studied this monument extensively for decades.",
    "personality": "Scholarly, wise, patient, and deeply passionate about history.",
    "speaking_style": "Eloquent, educational, and engaging with vivid descriptions."
}
