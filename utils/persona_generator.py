"""
Historical persona generator using Google Gemini AI
"""
import json
from google import genai
from google.genai import types
import config


class PersonaGenerator:
    def __init__(self, api_key: str, model: str = None):
        """Initialize the persona generator with Gemini API key"""
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key)
        self.model = model or config.DEFAULT_MODEL
        
    def generate_persona(self, landmark_info: dict) -> dict:
        """
        Generate a historical persona related to the landmark
        
        Args:
            landmark_info: Dictionary with landmark details
            
        Returns:
            dict: Persona details including name, title, era, etc.
        """
        try:
            prompt = f"""Based on this monument/landmark, create a compelling historical persona who has a deep connection to this place:

Monument: {landmark_info.get('landmark_name', 'Unknown')}
Location: {landmark_info.get('location', 'Unknown')}
Era: {landmark_info.get('era', 'Unknown')}
Description: {landmark_info.get('description', 'Unknown')}

Create ONE main historical figure who could have been the architect, builder, ruler, designer, or someone deeply connected to this monument.

Return ONLY a valid JSON object (no markdown, no code blocks) with this structure:
{{
    "name": "Full name of historical figure",
    "title": "Their role/title (e.g., Architect, Emperor, Engineer)",
    "era": "Time period they lived",
    "avatar": "Single emoji that represents them (👑, ⚒️, 📐, etc.)",
    "connection": "One sentence explaining their connection to the monument",
    "personality": "Brief description of their personality traits",
    "speaking_style": "How they speak (formal, passionate, scholarly, etc.)",
    "knowledge_cutoff": "What time period their knowledge covers",
    "region": "Geographic region (e.g., india, france, egypt, rome, greece)",
    "gender": "male/female/neutral"
}}

Be creative but historically plausible. Choose someone who would have fascinating stories."""

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            
            response_text = response.text.strip()
            
            # Clean markdown if present
            if response_text.startswith("```"):
                lines = response_text.split("\n")
                response_text = "\n".join(lines[1:-1])
            if response_text.startswith("json"):
                response_text = response_text[4:].strip()
            
            persona = json.loads(response_text)
            
            # Add system prompt
            persona['system_prompt'] = self._create_system_prompt(persona, landmark_info)
            
            return persona
            
        except Exception as e:
            print(f"Error generating persona: {e}")
            return self._get_fallback_persona(landmark_info)
    
    def generate_related_personas(self, landmark_info: dict, main_persona: dict) -> list:
        """
        Generate 3-4 alternative personas related to the same landmark
        
        Args:
            landmark_info: Dictionary with landmark details
            main_persona: The main persona already generated
            
        Returns:
            list: List of alternative persona dictionaries
        """
        try:
            prompt = f"""Based on this monument, create 3 DIFFERENT historical personas (not including {main_persona.get('name')}):

Monument: {landmark_info.get('landmark_name', 'Unknown')}
Location: {landmark_info.get('location', 'Unknown')}
Era: {landmark_info.get('era', 'Unknown')}

Create 3 different types of people:
1. A craftsman, artisan, or worker who built it
2. A patron, ruler, or sponsor who commissioned it
3. Someone who lived in or used the structure

Return ONLY a valid JSON array (no markdown, no code blocks) with 3 objects, each having:
{{
    "name": "Full name",
    "title": "Their role",
    "era": "Time period",
    "avatar": "Single emoji",
    "connection": "Their connection to monument",
    "personality": "Personality traits",
    "speaking_style": "Speaking style",
    "knowledge_cutoff": "Time period of knowledge",
    "region": "Geographic region",
    "gender": "male/female/neutral"
}}"""

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            
            response_text = response.text.strip()
            
            # Clean markdown if present
            if response_text.startswith("```"):
                lines = response_text.split("\n")
                response_text = "\n".join(lines[1:-1])
            if response_text.startswith("json"):
                response_text = response_text[4:].strip()
            
            personas = json.loads(response_text)
            
            # Add system prompts
            for persona in personas:
                persona['system_prompt'] = self._create_system_prompt(persona, landmark_info)
            
            return personas
            
        except Exception as e:
            print(f"Error generating related personas: {e}")
            return []
    
    def _create_system_prompt(self, persona: dict, landmark_info: dict) -> str:
        """Create detailed system prompt for the persona"""
        return f"""You are {persona.get('name')}, {persona.get('title')}.

MONUMENT CONNECTION:
{persona.get('connection')}

HISTORICAL CONTEXT:
- You lived during: {persona.get('era')}
- Monument: {landmark_info.get('landmark_name')}
- Location: {landmark_info.get('location')}
- Your knowledge is limited to events up to: {persona.get('knowledge_cutoff', persona.get('era'))}

PERSONALITY:
{persona.get('personality')}

SPEAKING STYLE:
{persona.get('speaking_style')}

INSTRUCTIONS:
1. Stay in character at all times
2. Share personal stories and experiences related to the monument
3. Speak from first-person perspective about your era
4. Don't break character or mention you're an AI
5. Use vivid, immersive language to bring history alive
6. Share historical details, anecdotes, and cultural context
7. Express emotions and opinions authentic to your time period
8. If asked about events after your time, politely explain you lived before then
9. Make the conversation engaging and educational
10. Use period-appropriate language and references"""
    
    def generate_greeting(self, persona: dict, landmark_info: dict) -> str:
        """Generate an initial greeting from the persona"""
        try:
            prompt = f"""You are {persona.get('name')}, {persona.get('title')}.
Your connection: {persona.get('connection')}
Monument: {landmark_info.get('landmark_name')}

Write a warm, engaging greeting (2-3 sentences) introducing yourself to someone interested in this monument.
Be welcoming, hint at your personal connection, and invite them to ask you questions.
Stay in character. DO NOT use markdown formatting."""

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            
            return response.text.strip()
            
        except Exception as e:
            print(f"Error generating greeting: {e}")
            return f"Greetings! I am {persona.get('name')}, {persona.get('title')}. I have a deep connection to {landmark_info.get('landmark_name')}. Ask me anything about this magnificent place!"
    
    def generate_response(self, persona: dict, landmark_info: dict, chat_history: list, user_message: str) -> str:
        """
        Generate a response from the persona to user's message
        
        Args:
            persona: Persona dictionary
            landmark_info: Landmark information
            chat_history: List of previous messages
            user_message: User's current message
            
        Returns:
            str: Persona's response
        """
        try:
            # Build conversation context
            context = persona.get('system_prompt', '')
            context += f"\n\nMONUMENT DETAILS:\n"
            context += f"Name: {landmark_info.get('landmark_name')}\n"
            context += f"Location: {landmark_info.get('location')}\n"
            context += f"Era: {landmark_info.get('era')}\n"
            context += f"Description: {landmark_info.get('description')}\n"
            context += f"Significance: {landmark_info.get('historical_significance', 'N/A')}\n"
            
            # Add recent chat history (last 5 exchanges)
            if chat_history:
                context += "\n\nRECENT CONVERSATION:\n"
                for msg in chat_history[-10:]:  # Last 10 messages
                    role = msg.get('role', 'user')
                    content = msg.get('content', '')
                    context += f"{role.upper()}: {content}\n"
            
            # Create the prompt
            prompt = f"""{context}

USER'S QUESTION: {user_message}

Respond as {persona.get('name')} in character. Be engaging, educational, and historically accurate.
Keep responses concise (2-4 sentences) unless the question requires detail.
DO NOT use markdown formatting - just plain text."""

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            
            return response.text.strip()
            
        except Exception as e:
            print(f"Error generating response: {e}")
            return f"Forgive me, I seem to have lost my train of thought. Could you ask that again?"
    
    def _get_fallback_persona(self, landmark_info: dict) -> dict:
        """Return fallback persona when generation fails"""
        fallback = config.FALLBACK_PERSONA.copy()
        fallback['system_prompt'] = self._create_system_prompt(fallback, landmark_info)
        fallback['knowledge_cutoff'] = "Present Day"
        fallback['region'] = "global"
        fallback['gender'] = "neutral"
        return fallback
