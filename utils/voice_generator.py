"""
Voice generator for text-to-speech using gTTS
"""
import base64
import io
import re
from gtts import gTTS
import config


class VoiceGenerator:
    def __init__(self):
        """Initialize voice generator"""
        # Language mapping based on region
        self.language_map = {
            'india': 'en',
            'france': 'fr',
            'spain': 'es',
            'italy': 'it',
            'germany': 'de',
            'russia': 'ru',
            'china': 'zh-CN',
            'japan': 'ja',
            'korea': 'ko',
            'egypt': 'ar',
            'greece': 'el',
            'rome': 'it',
            'england': 'en',
            'uk': 'en',
            'usa': 'en',
            'mexico': 'es',
            'brazil': 'pt',
            'portugal': 'pt',
            'turkey': 'tr',
            'default': 'en'
        }
    
    def generate_speech(self, text: str, persona: dict = None) -> str:
        """
        Generate speech audio from text
        
        Args:
            text: Text to convert to speech
            persona: Optional persona dictionary to determine language
            
        Returns:
            str: Base64 encoded audio data
        """
        try:
            # Clean text for speech
            clean_text = self._clean_text_for_speech(text)
            
            if not clean_text.strip():
                return ""
            
            # Get language for persona
            lang = self._get_language_for_persona(persona)
            
            # Generate speech
            tts = gTTS(text=clean_text, lang=lang, slow=config.VOICE_SLOW)
            
            # Convert to bytes
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            
            # Encode to base64
            audio_base64 = base64.b64encode(audio_fp.read()).decode('utf-8')
            
            return audio_base64
            
        except Exception as e:
            print(f"Error generating speech: {e}")
            return ""
    
    def _clean_text_for_speech(self, text: str) -> str:
        """Clean text for better speech synthesis"""
        # Remove markdown formatting
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)  # Bold
        text = re.sub(r'\*(.+?)\*', r'\1', text)  # Italic
        text = re.sub(r'`(.+?)`', r'\1', text)  # Code
        text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)  # Links
        
        # Remove emojis and special characters
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Limit length for TTS (gTTS has limits)
        max_chars = 5000
        if len(text) > max_chars:
            text = text[:max_chars] + "..."
        
        return text
    
    def _get_language_for_persona(self, persona: dict) -> str:
        """Determine language based on persona's region"""
        if not persona:
            return config.DEFAULT_VOICE_LANG
        
        region = persona.get('region', '').lower()
        
        # Check if region is in our language map
        for key, lang in self.language_map.items():
            if key in region:
                return lang
        
        # Default to English
        return config.DEFAULT_VOICE_LANG
    
    def get_audio_html(self, audio_base64: str, autoplay: bool = False) -> str:
        """
        Generate HTML audio player
        
        Args:
            audio_base64: Base64 encoded audio data
            autoplay: Whether to autoplay the audio
            
        Returns:
            str: HTML audio player code
        """
        if not audio_base64:
            return ""
        
        autoplay_attr = "autoplay" if autoplay else ""
        
        html = f"""
        <audio controls {autoplay_attr} style="width: 100%; margin: 10px 0; border-radius: 10px;">
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
        """
        
        return html
