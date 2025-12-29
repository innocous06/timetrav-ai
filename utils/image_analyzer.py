"""
Image analyzer for monument identification using Google Gemini AI
"""
import json
import io
from PIL import Image
from google import genai
from google.genai import types
import config


class ImageAnalyzer:
    def __init__(self, api_key: str, model: str = None):
        """Initialize the image analyzer with Gemini API key"""
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key)
        self.model = model or config.DEFAULT_MODEL
        
    def analyze_monument(self, image_data) -> dict:
        """
        Analyze monument image and extract information
        
        Args:
            image_data: PIL Image or file upload object
            
        Returns:
            dict: Monument information including name, location, era, etc.
        """
        try:
            # Convert to PIL Image if needed
            if not isinstance(image_data, Image.Image):
                image = Image.open(image_data)
            else:
                image = image_data
            
            # Resize if needed to respect max size
            max_size = config.MAX_IMAGE_SIZE
            if image.size[0] > max_size[0] or image.size[1] > max_size[1]:
                image.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Convert to bytes
            img_byte_arr = io.BytesIO()
            image_format = image.format if image.format else 'PNG'
            image.save(img_byte_arr, format=image_format)
            image_bytes = img_byte_arr.getvalue()
            
            # Determine MIME type
            mime_type = f"image/{image_format.lower()}"
            if mime_type == "image/jpg":
                mime_type = "image/jpeg"
            
            # Create prompt for monument analysis
            prompt = """Analyze this image and identify the monument or landmark. 
            Return ONLY a valid JSON object (no markdown, no code blocks) with the following structure:
            {
                "landmark_name": "Full name of the monument/landmark",
                "location": "City, Country or region",
                "architectural_style": "Style of architecture (e.g., Gothic, Roman, Modern)",
                "era": "Time period or century (e.g., 12th Century, Ancient Rome)",
                "description": "Brief 2-3 sentence description",
                "visual_elements": "Key visual features you observe",
                "confidence": "high/medium/low - your confidence in identification",
                "historical_significance": "Why this monument is historically important"
            }
            
            If you cannot identify the specific monument, still provide your best analysis based on architectural features visible."""
            
            # Call Gemini API with new SDK
            response = self.client.models.generate_content(
                model=self.model,
                contents=[
                    types.Content(
                        role="user",
                        parts=[
                            types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
                            types.Part.from_text(text=prompt)
                        ]
                    )
                ]
            )
            
            # Extract and parse response
            response_text = response.text.strip()
            
            # Remove markdown code blocks if present
            if response_text.startswith("```"):
                lines = response_text.split("\n")
                response_text = "\n".join(lines[1:-1])
            if response_text.startswith("json"):
                response_text = response_text[4:].strip()
            
            # Parse JSON
            monument_info = json.loads(response_text)
            
            # Validate required fields
            required_fields = ["landmark_name", "location", "era", "description"]
            for field in required_fields:
                if field not in monument_info:
                    monument_info[field] = "Unknown"
            
            return monument_info
            
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return self._get_fallback_info()
        except Exception as e:
            print(f"Error analyzing image: {e}")
            return self._get_fallback_info()
    
    def _get_fallback_info(self) -> dict:
        """Return fallback information when analysis fails"""
        return {
            "landmark_name": "Unknown Monument",
            "location": "Unknown Location",
            "architectural_style": "Unknown Style",
            "era": "Unknown Era",
            "description": "Unable to identify this monument. Please try another image or check your API key.",
            "visual_elements": "Image analysis unavailable",
            "confidence": "low",
            "historical_significance": "Unable to determine at this time."
        }
