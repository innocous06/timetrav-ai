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

# Available Gemini models (all support multimodal/image input)
AVAILABLE_MODELS = {
    "gemini-2.5-flash": "Gemini 2.5 Flash (Recommended)",
    "gemini-2.5-flash-lite": "Gemini 2.5 Flash Lite (Fastest)",
    "gemini-3-flash": "Gemini 3 Flash (Latest)"
}
DEFAULT_MODEL = "gemini-2.5-flash"
# Backward compatibility
GEMINI_MODEL = DEFAULT_MODEL

FALLBACK_PERSONA = {
    "name": "Ancient Historian",
    "title": "Keeper of History",
    "era": "Timeless",
    "avatar": "📜",
    "connection": "I have studied this monument extensively for decades.",
    "personality": "Scholarly, wise, patient, and deeply passionate about history.",
    "speaking_style": "Eloquent, educational, and engaging with vivid descriptions."
}

# API Network Timeout Settings
API_TIMEOUT_SECONDS = 15
MAX_RETRY_ATTEMPTS = 3
