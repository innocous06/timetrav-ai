"""
Immersive mode component for cinematic display
"""


class ImmersiveMode:
    def __init__(self):
        """Initialize immersive mode generator"""
        pass
    
    def generate_immersive_html(self, persona: dict, message: str, images: list, audio_base64: str = None) -> str:
        """
        Generate immersive HTML experience
        
        Args:
            persona: Persona dictionary with name, title, era, avatar
            message: Text message to display as subtitles
            images: List of image dictionaries with 'url' and 'caption'
            audio_base64: Optional base64 encoded audio
            
        Returns:
            str: Complete HTML document for immersive display
        """
        # Prepare images for slideshow
        image_html = ""
        for i, img in enumerate(images):
            active_class = "active" if i == 0 else ""
            image_html += f"""
            <div class="slide {active_class}">
                <img src="{img['url']}" alt="{img.get('caption', '')}">
            </div>
            """
        
        # Navigation dots
        dots_html = ""
        for i in range(len(images)):
            active_class = "active" if i == 0 else ""
            dots_html += f'<span class="dot {active_class}" onclick="currentSlide({i + 1})"></span>'
        
        # Audio element
        audio_html = ""
        if audio_base64:
            audio_html = f"""
            <audio id="immersiveAudio" autoplay>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
            """
        
        # Audio visualizer bars
        visualizer_bars = ""
        for i in range(20):
            visualizer_bars += '<div class="bar"></div>'
        
        # Complete HTML
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                
                body {{
                    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
                    color: white;
                    font-family: 'Arial', sans-serif;
                    overflow: hidden;
                    height: 100vh;
                }}
                
                .container {{
                    position: relative;
                    width: 100%;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }}
                
                /* Slideshow container */
                .slideshow-container {{
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    z-index: 1;
                }}
                
                .slide {{
                    display: none;
                    width: 100%;
                    height: 100%;
                    position: absolute;
                    top: 0;
                    left: 0;
                    animation: fadeIn 1s ease-in-out;
                }}
                
                .slide.active {{
                    display: block;
                }}
                
                .slide img {{
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                    filter: brightness(0.6);
                }}
                
                @keyframes fadeIn {{
                    from {{ opacity: 0; }}
                    to {{ opacity: 1; }}
                }}
                
                /* Navigation arrows */
                .prev, .next {{
                    cursor: pointer;
                    position: absolute;
                    top: 50%;
                    width: auto;
                    margin-top: -22px;
                    padding: 16px;
                    color: white;
                    font-weight: bold;
                    font-size: 24px;
                    transition: 0.3s ease;
                    border-radius: 0 3px 3px 0;
                    user-select: none;
                    z-index: 10;
                    background-color: rgba(0,0,0,0.3);
                }}
                
                .next {{
                    right: 0;
                    border-radius: 3px 0 0 3px;
                }}
                
                .prev:hover, .next:hover {{
                    background-color: rgba(0,0,0,0.6);
                }}
                
                /* Dots */
                .dots-container {{
                    position: absolute;
                    bottom: 150px;
                    left: 50%;
                    transform: translateX(-50%);
                    z-index: 10;
                    display: flex;
                    gap: 10px;
                }}
                
                .dot {{
                    cursor: pointer;
                    height: 12px;
                    width: 12px;
                    background-color: rgba(255, 255, 255, 0.3);
                    border-radius: 50%;
                    display: inline-block;
                    transition: all 0.3s ease;
                }}
                
                .dot.active, .dot:hover {{
                    background-color: rgba(78, 205, 196, 0.9);
                    transform: scale(1.3);
                }}
                
                /* Persona info overlay */
                .persona-overlay {{
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    z-index: 5;
                    text-align: center;
                    animation: floatIn 1.5s ease-out;
                }}
                
                @keyframes floatIn {{
                    from {{
                        opacity: 0;
                        transform: translate(-50%, -40%);
                    }}
                    to {{
                        opacity: 1;
                        transform: translate(-50%, -50%);
                    }}
                }}
                
                .persona-avatar {{
                    font-size: 6rem;
                    margin-bottom: 1rem;
                    text-shadow: 0 0 30px rgba(78, 205, 196, 0.8);
                    animation: pulse 2s ease-in-out infinite;
                }}
                
                @keyframes pulse {{
                    0%, 100% {{ transform: scale(1); }}
                    50% {{ transform: scale(1.1); }}
                }}
                
                .persona-name {{
                    font-size: 3rem;
                    font-weight: bold;
                    text-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
                    margin-bottom: 0.5rem;
                    color: #4ecdc4;
                }}
                
                .persona-title {{
                    font-size: 1.5rem;
                    font-style: italic;
                    text-shadow: 0 0 15px rgba(0, 0, 0, 0.8);
                    margin-bottom: 0.5rem;
                    color: #45b7d1;
                }}
                
                .persona-era {{
                    font-size: 1.2rem;
                    text-shadow: 0 0 15px rgba(0, 0, 0, 0.8);
                    color: #b8b8b8;
                }}
                
                /* Audio visualizer */
                .visualizer {{
                    position: absolute;
                    bottom: 250px;
                    left: 50%;
                    transform: translateX(-50%);
                    display: flex;
                    gap: 4px;
                    align-items: flex-end;
                    height: 60px;
                    z-index: 10;
                    opacity: 0.7;
                }}
                
                .bar {{
                    width: 4px;
                    background: linear-gradient(to top, #4ecdc4, #45b7d1);
                    border-radius: 2px;
                    animation: wave 1s ease-in-out infinite;
                    height: 10px;
                }}
                
                .bar:nth-child(1) {{ animation-delay: 0s; }}
                .bar:nth-child(2) {{ animation-delay: 0.1s; }}
                .bar:nth-child(3) {{ animation-delay: 0.2s; }}
                .bar:nth-child(4) {{ animation-delay: 0.3s; }}
                .bar:nth-child(5) {{ animation-delay: 0.4s; }}
                .bar:nth-child(6) {{ animation-delay: 0.5s; }}
                .bar:nth-child(7) {{ animation-delay: 0.6s; }}
                .bar:nth-child(8) {{ animation-delay: 0.7s; }}
                .bar:nth-child(9) {{ animation-delay: 0.8s; }}
                .bar:nth-child(10) {{ animation-delay: 0.9s; }}
                .bar:nth-child(11) {{ animation-delay: 1s; }}
                .bar:nth-child(12) {{ animation-delay: 0.9s; }}
                .bar:nth-child(13) {{ animation-delay: 0.8s; }}
                .bar:nth-child(14) {{ animation-delay: 0.7s; }}
                .bar:nth-child(15) {{ animation-delay: 0.6s; }}
                .bar:nth-child(16) {{ animation-delay: 0.5s; }}
                .bar:nth-child(17) {{ animation-delay: 0.4s; }}
                .bar:nth-child(18) {{ animation-delay: 0.3s; }}
                .bar:nth-child(19) {{ animation-delay: 0.2s; }}
                .bar:nth-child(20) {{ animation-delay: 0.1s; }}
                
                @keyframes wave {{
                    0%, 100% {{ height: 10px; }}
                    50% {{ height: 50px; }}
                }}
                
                /* Subtitles */
                .subtitles {{
                    position: absolute;
                    bottom: 50px;
                    left: 50%;
                    transform: translateX(-50%);
                    width: 80%;
                    max-width: 900px;
                    background: rgba(0, 0, 0, 0.8);
                    padding: 20px 30px;
                    border-radius: 15px;
                    text-align: center;
                    font-size: 1.2rem;
                    line-height: 1.6;
                    z-index: 10;
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
                    animation: slideUp 1s ease-out;
                }}
                
                @keyframes slideUp {{
                    from {{
                        opacity: 0;
                        transform: translate(-50%, 20px);
                    }}
                    to {{
                        opacity: 1;
                        transform: translate(-50%, 0);
                    }}
                }}
                
                /* Close button */
                .close-btn {{
                    position: absolute;
                    top: 20px;
                    right: 20px;
                    font-size: 2rem;
                    color: white;
                    cursor: pointer;
                    z-index: 20;
                    background: rgba(255, 107, 107, 0.7);
                    width: 50px;
                    height: 50px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    transition: all 0.3s ease;
                }}
                
                .close-btn:hover {{
                    background: rgba(255, 107, 107, 0.9);
                    transform: rotate(90deg);
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <!-- Slideshow -->
                <div class="slideshow-container">
                    {image_html}
                    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
                    <a class="next" onclick="plusSlides(1)">&#10095;</a>
                </div>
                
                <!-- Persona overlay -->
                <div class="persona-overlay">
                    <div class="persona-avatar">{persona.get('avatar', '🏛️')}</div>
                    <div class="persona-name">{persona.get('name', 'Unknown')}</div>
                    <div class="persona-title">{persona.get('title', '')}</div>
                    <div class="persona-era">{persona.get('era', '')}</div>
                </div>
                
                <!-- Audio visualizer -->
                {('<div class="visualizer">' + visualizer_bars + '</div>') if audio_base64 else ''}
                
                <!-- Dots -->
                <div class="dots-container">
                    {dots_html}
                </div>
                
                <!-- Subtitles -->
                <div class="subtitles">
                    {message}
                </div>
                
                <!-- Close button -->
                <div class="close-btn" onclick="window.parent.postMessage('close_immersive', '*')">×</div>
                
                <!-- Audio element -->
                {audio_html}
            </div>
            
            <script>
                let slideIndex = 1;
                let autoAdvanceTimer;
                
                // Show first slide
                showSlides(slideIndex);
                
                // Start auto-advance
                startAutoAdvance();
                
                function plusSlides(n) {{
                    showSlides(slideIndex += n);
                    resetAutoAdvance();
                }}
                
                function currentSlide(n) {{
                    showSlides(slideIndex = n);
                    resetAutoAdvance();
                }}
                
                function showSlides(n) {{
                    let slides = document.getElementsByClassName("slide");
                    let dots = document.getElementsByClassName("dot");
                    
                    if (n > slides.length) {{ slideIndex = 1 }}
                    if (n < 1) {{ slideIndex = slides.length }}
                    
                    for (let i = 0; i < slides.length; i++) {{
                        slides[i].classList.remove("active");
                    }}
                    
                    for (let i = 0; i < dots.length; i++) {{
                        dots[i].classList.remove("active");
                    }}
                    
                    if (slides.length > 0) {{
                        slides[slideIndex - 1].classList.add("active");
                    }}
                    if (dots.length > 0) {{
                        dots[slideIndex - 1].classList.add("active");
                    }}
                }}
                
                function startAutoAdvance() {{
                    autoAdvanceTimer = setInterval(() => {{
                        plusSlides(1);
                    }}, 6000); // 6 seconds
                }}
                
                function resetAutoAdvance() {{
                    clearInterval(autoAdvanceTimer);
                    startAutoAdvance();
                }}
                
                // Keyboard navigation
                document.addEventListener('keydown', (e) => {{
                    if (e.key === 'ArrowLeft') {{
                        plusSlides(-1);
                    }} else if (e.key === 'ArrowRight') {{
                        plusSlides(1);
                    }} else if (e.key === 'Escape') {{
                        window.parent.postMessage('close_immersive', '*');
                    }}
                }});
            </script>
        </body>
        </html>
        """
        
        return html
