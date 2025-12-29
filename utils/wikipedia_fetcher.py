"""
Wikipedia image fetcher for monument photos
"""
import requests
from bs4 import BeautifulSoup
import urllib.parse
import config


class WikipediaFetcher:
    def __init__(self):
        """Initialize Wikipedia fetcher"""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'TimeTravelAI/1.0 (Educational Project)'
        })
        self._cache = {}
        
    def fetch_images(self, landmark_name: str, count: int = 5) -> list:
        """
        Fetch images from Wikipedia for the given landmark
        
        Args:
            landmark_name: Name of the landmark to search
            count: Number of images to fetch
            
        Returns:
            list: List of dictionaries with 'url' and 'caption' keys
        """
        # Check cache first
        cache_key = f"{landmark_name}_{count}"
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        try:
            # Search Wikipedia for the landmark
            search_url = "https://en.wikipedia.org/w/api.php"
            search_params = {
                'action': 'opensearch',
                'search': landmark_name,
                'limit': 1,
                'format': 'json'
            }
            
            response = self.session.get(search_url, params=search_params, timeout=10)
            response.raise_for_status()
            search_results = response.json()
            
            if not search_results[1]:  # No results found
                return self._get_placeholder_images(landmark_name)
            
            # Get the page title
            page_title = search_results[1][0]
            
            # Fetch images from the page
            images_url = "https://en.wikipedia.org/w/api.php"
            images_params = {
                'action': 'query',
                'titles': page_title,
                'prop': 'images',
                'imlimit': 50,
                'format': 'json'
            }
            
            response = self.session.get(images_url, params=images_params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            pages = data.get('query', {}).get('pages', {})
            if not pages:
                return self._get_placeholder_images(landmark_name)
            
            page_id = list(pages.keys())[0]
            images = pages[page_id].get('images', [])
            
            # Filter and get image URLs
            image_list = []
            for img in images:
                image_name = img.get('title', '')
                
                # Skip non-relevant images
                if not self._is_valid_image(image_name):
                    continue
                
                # Get actual image URL
                image_url = self._get_image_url(image_name)
                if image_url:
                    image_list.append({
                        'url': image_url,
                        'caption': self._clean_image_name(image_name)
                    })
                
                if len(image_list) >= count:
                    break
            
            # If we didn't get enough images, add placeholders
            if len(image_list) < count:
                placeholder_count = count - len(image_list)
                image_list.extend(self._get_placeholder_images(landmark_name)[:placeholder_count])
            
            # Cache the results
            self._cache[cache_key] = image_list
            
            return image_list
            
        except Exception as e:
            print(f"Error fetching Wikipedia images: {e}")
            return self._get_placeholder_images(landmark_name)
    
    def _is_valid_image(self, image_name: str) -> bool:
        """Check if image is valid (not icon, logo, map, etc.)"""
        image_name_lower = image_name.lower()
        
        # Skip common non-photo images
        skip_patterns = [
            'icon', 'logo', 'flag', 'map', 'diagram', 
            'chart', 'graph', 'symbol', '.svg', 'commons-logo',
            'wikimedia', 'wiki', 'edit', 'question'
        ]
        
        for pattern in skip_patterns:
            if pattern in image_name_lower:
                return False
        
        # Only accept common image formats
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        if not any(ext in image_name_lower for ext in valid_extensions):
            return False
        
        return True
    
    def _get_image_url(self, image_name: str) -> str:
        """Get the actual URL for a Wikipedia image"""
        try:
            info_url = "https://en.wikipedia.org/w/api.php"
            info_params = {
                'action': 'query',
                'titles': image_name,
                'prop': 'imageinfo',
                'iiprop': 'url',
                'iiurlwidth': 800,
                'format': 'json'
            }
            
            response = self.session.get(info_url, params=info_params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            pages = data.get('query', {}).get('pages', {})
            if pages:
                page_id = list(pages.keys())[0]
                imageinfo = pages[page_id].get('imageinfo', [])
                if imageinfo:
                    return imageinfo[0].get('thumburl', imageinfo[0].get('url', ''))
            
            return ''
            
        except Exception as e:
            print(f"Error getting image URL: {e}")
            return ''
    
    def _clean_image_name(self, image_name: str) -> str:
        """Clean image name to create a caption"""
        # Remove "File:" prefix
        name = image_name.replace('File:', '').replace('Image:', '')
        
        # Remove extension
        for ext in ['.jpg', '.jpeg', '.png', '.gif', '.JPG', '.JPEG', '.PNG', '.GIF']:
            name = name.replace(ext, '')
        
        # Replace underscores with spaces
        name = name.replace('_', ' ')
        
        # Limit length
        if len(name) > 50:
            name = name[:47] + "..."
        
        return name
    
    def _get_placeholder_images(self, landmark_name: str) -> list:
        """Generate placeholder images when Wikipedia fetch fails"""
        # Use picsum.photos for placeholder images with different seeds
        placeholders = []
        for i in range(config.WIKIPEDIA_IMAGE_COUNT):
            seed = abs(hash(landmark_name + str(i))) % 1000
            placeholders.append({
                'url': f'https://picsum.photos/seed/{seed}/800/600',
                'caption': f'{landmark_name} - View {i+1}'
            })
        
        return placeholders
