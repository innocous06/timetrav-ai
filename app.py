"""
TimeTraveler AI - Immersive Historical Storytelling Platform
Where History Speaks Through Those Who Made It
"""
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import config
from styles import get_custom_css
from utils import (
    ImageAnalyzer,
    PersonaGenerator,
    WikipediaFetcher,
    VoiceGenerator,
    ImmersiveMode
)


# Page configuration
st.set_page_config(
    page_title=config.APP_NAME,
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)


def init_session_state():
    """Initialize session state variables"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'current_persona' not in st.session_state:
        st.session_state.current_persona = None
    if 'related_personas' not in st.session_state:
        st.session_state.related_personas = []
    if 'landmark_info' not in st.session_state:
        st.session_state.landmark_info = None
    if 'landmark_images' not in st.session_state:
        st.session_state.landmark_images = []
    if 'voice_settings' not in st.session_state:
        st.session_state.voice_settings = {'enabled': True}
    if 'audio_enabled' not in st.session_state:
        st.session_state.audio_enabled = True
    if 'immersive_mode' not in st.session_state:
        st.session_state.immersive_mode = False
    if 'greeted' not in st.session_state:
        st.session_state.greeted = False
    if 'api_configured' not in st.session_state:
        st.session_state.api_configured = False
    if 'api_key' not in st.session_state:
        st.session_state.api_key = config.GOOGLE_API_KEY
    if 'selected_model' not in st.session_state:
        st.session_state.selected_model = config.DEFAULT_MODEL
    if 'needs_monument_clarification' not in st.session_state:
        st.session_state.needs_monument_clarification = False
    if 'partial_visual_info' not in st.session_state:
        st.session_state.partial_visual_info = None


def reset_session():
    """Reset session for a new journey"""
    st.session_state.chat_history = []
    st.session_state.current_persona = None
    st.session_state.related_personas = []
    st.session_state.landmark_info = None
    st.session_state.landmark_images = []
    st.session_state.greeted = False
    st.session_state.needs_monument_clarification = False
    st.session_state.partial_visual_info = None
    st.rerun()


def switch_persona(new_persona: dict):
    """Switch to a different historical persona"""
    st.session_state.current_persona = new_persona
    st.session_state.chat_history = []
    st.session_state.greeted = False
    st.rerun()


def process_user_message(user_message: str):
    """Process user message and generate response"""
    if not user_message.strip():
        return
    
    # Add user message to history
    st.session_state.chat_history.append({
        'role': 'user',
        'content': user_message
    })
    
    # Generate response
    try:
        persona_gen = PersonaGenerator(st.session_state.api_key, st.session_state.selected_model)
        response = persona_gen.generate_response(
            st.session_state.current_persona,
            st.session_state.landmark_info,
            st.session_state.chat_history,
            user_message
        )
        
        # Add AI response to history
        st.session_state.chat_history.append({
            'role': 'assistant',
            'content': response
        })
        
    except Exception as e:
        st.error(f"Error generating response: {e}")


def main():
    """Main application"""
    init_session_state()
    
    # Apply custom CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # Header
    st.markdown(f'<h1 class="main-header">{config.APP_NAME}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="subtitle">{config.APP_SUBTITLE}</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        
        # API Key input
        api_key_input = st.text_input(
            "Google Gemini API Key",
            type="password",
            value=st.session_state.api_key,
            help="Get your free API key from: https://aistudio.google.com/app/apikey"
        )
        
        if api_key_input != st.session_state.api_key:
            st.session_state.api_key = api_key_input
            st.session_state.api_configured = bool(api_key_input.strip())
        
        if st.session_state.api_key:
            st.success("✅ API Key Configured")
            st.session_state.api_configured = True
        else:
            st.warning("⚠️ API Key Required")
            st.session_state.api_configured = False
        
        st.markdown("---")
        
        # Model Selection
        st.markdown("#### 🤖 AI Model")
        
        model_options = list(config.AVAILABLE_MODELS.keys())
        model_labels = list(config.AVAILABLE_MODELS.values())
        
        # Get current index
        current_model = st.session_state.get('selected_model', config.DEFAULT_MODEL)
        current_index = model_options.index(current_model) if current_model in model_options else 0
        
        selected_label = st.selectbox(
            "Select Gemini Model",
            options=model_labels,
            index=current_index,
            help="Switch models if you hit rate limits"
        )
        
        # Update session state with the model key
        selected_model = model_options[model_labels.index(selected_label)]
        st.session_state.selected_model = selected_model
        
        st.caption(f"💡 Using: `{selected_model}`")
        
        st.markdown("---")
        
        # Voice narration toggle
        st.markdown("### 🔊 Voice Narration")
        audio_enabled = st.checkbox(
            "Enable voice narration",
            value=st.session_state.audio_enabled
        )
        st.session_state.audio_enabled = audio_enabled
        
        # Immersive mode toggle
        st.markdown("### 🎬 Immersive Mode")
        immersive_enabled = st.checkbox(
            "Enable cinematic experience",
            value=st.session_state.immersive_mode,
            help="Full-screen experience with images and audio"
        )
        st.session_state.immersive_mode = immersive_enabled
        
        # Related personas
        if st.session_state.related_personas:
            st.markdown("---")
            st.markdown("### 🎭 Other Voices")
            st.markdown("*Switch to hear from:*")
            
            for persona in st.session_state.related_personas:
                if st.button(
                    f"{persona['avatar']} {persona['name']}",
                    key=f"persona_{persona['name']}",
                    use_container_width=True
                ):
                    switch_persona(persona)
        
        # New Journey button
        if st.session_state.current_persona:
            st.markdown("---")
            if st.button("🔄 New Journey", use_container_width=True):
                reset_session()
        
        # Credits
        st.markdown("---")
        st.markdown("### 💡 About")
        st.markdown("""
        **TimeTraveler AI** brings history to life through AI-generated historical personas.
        
        Powered by:
        - Google Gemini AI
        - Streamlit
        - Wikipedia
        - gTTS
        """)
    
    # Main content area - Two columns
    col_left, col_right = st.columns([1, 1])
    
    # Left Column - Discovery
    with col_left:
        st.markdown("### 📸 Monument Discovery")
        
        if not st.session_state.api_configured:
            st.warning("⚠️ Please enter your Google Gemini API key in the sidebar to begin.")
            st.info("Get your free API key from: https://aistudio.google.com/app/apikey")
        else:
            # Input method selector
            input_method = st.radio(
                "How would you like to discover a monument?",
                ["📸 Upload an Image", "✍️ Enter Monument Name"],
                horizontal=True
            )
            
            if input_method == "📸 Upload an Image":
                # File uploader
                uploaded_file = st.file_uploader(
                    "Upload a photo of a historical monument",
                    type=['jpg', 'jpeg', 'png'],
                    help="Upload a clear photo of any historical monument or landmark"
                )
                
                if uploaded_file:
                    # Display uploaded image
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Uploaded Monument", use_container_width=True)
                    
                    # Analyze button
                    if st.button("🔍 Identify & Summon Historical Guide", use_container_width=True):
                        with st.spinner("🔮 Analyzing monument and summoning historical guide..."):
                            try:
                                # Analyze image
                                analyzer = ImageAnalyzer(st.session_state.api_key, st.session_state.selected_model)
                                landmark_info = analyzer.analyze_monument(uploaded_file)
                                
                                # Check confidence - if low, ask for clarification
                                if landmark_info.get('confidence') == 'low' or landmark_info.get('landmark_name') in ['Historical Monument', 'Unknown Monument', 'Unknown']:
                                    # Don't generate persona yet - set clarification flag
                                    st.session_state.landmark_info = None
                                    st.session_state.needs_monument_clarification = True
                                    st.session_state.partial_visual_info = landmark_info.get('visual_elements', '')
                                    st.rerun()
                                else:
                                    # Proceed normally with high confidence
                                    st.session_state.landmark_info = landmark_info
                                    
                                    # Generate main persona
                                    persona_gen = PersonaGenerator(st.session_state.api_key, st.session_state.selected_model)
                                    main_persona = persona_gen.generate_persona(landmark_info)
                                    st.session_state.current_persona = main_persona
                                    
                                    # Generate related personas
                                    related = persona_gen.generate_related_personas(landmark_info, main_persona)
                                    st.session_state.related_personas = related
                                    
                                    # Fetch Wikipedia images
                                    wiki_fetcher = WikipediaFetcher()
                                    images = wiki_fetcher.fetch_images(
                                        landmark_info.get('landmark_name', 'Unknown'),
                                        config.WIKIPEDIA_IMAGE_COUNT
                                    )
                                    st.session_state.landmark_images = images
                                    
                                    # Reset chat and greeting flag
                                    st.session_state.chat_history = []
                                    st.session_state.greeted = False
                                    
                                    st.success("✨ Historical guide summoned successfully!")
                                    st.rerun()
                                
                            except Exception as e:
                                st.error(f"Error: {e}")
            
            elif input_method == "✍️ Enter Monument Name":
                monument_name = st.text_input(
                    "Enter monument name",
                    placeholder="e.g., Taj Mahal, Colosseum, Eiffel Tower..."
                )
                
                if monument_name and st.button("🔮 Summon Historical Guide", use_container_width=True):
                    # Create landmark_info from text input (no image analysis needed)
                    with st.spinner("🔍 Researching monument..."):
                        try:
                            generator = PersonaGenerator(st.session_state.api_key, st.session_state.selected_model)
                            landmark_info = generator.research_monument(monument_name)
                            st.session_state.landmark_info = landmark_info
                            
                            # Continue with persona generation as usual
                            with st.spinner("👻 Summoning historical figure..."):
                                persona = generator.generate_persona(landmark_info)
                                st.session_state.current_persona = persona
                                related = generator.generate_related_personas(landmark_info, persona)
                                st.session_state.related_personas = related
                            
                            # Fetch images from Wikipedia
                            with st.spinner("🖼️ Gathering monument images..."):
                                fetcher = WikipediaFetcher()
                                images = fetcher.fetch_images(
                                    landmark_info.get('landmark_name', monument_name),
                                    config.WIKIPEDIA_IMAGE_COUNT
                                )
                                st.session_state.landmark_images = images
                            
                            st.session_state.chat_history = []
                            st.session_state.greeted = False
                            st.success("✨ Historical guide summoned successfully!")
                            st.rerun()
                            
                        except Exception as e:
                            st.error(f"Error: {e}")
            
            # Display landmark info if available
            if st.session_state.landmark_info:
                st.markdown("---")
                st.markdown("### 🏛️ Monument Information")
                
                info = st.session_state.landmark_info
                st.markdown(f'<div class="landmark-info">', unsafe_allow_html=True)
                st.markdown(f'<div class="landmark-name">{info.get("landmark_name", "Unknown")}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="landmark-detail">📍 {info.get("location", "Unknown")}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="landmark-detail">🏗️ {info.get("architectural_style", "Unknown")}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="landmark-detail">📅 {info.get("era", "Unknown")}</div>', unsafe_allow_html=True)
                st.markdown(f'</div>', unsafe_allow_html=True)
                
                with st.expander("📖 More Details"):
                    st.write(f"**Description:** {info.get('description', 'N/A')}")
                    st.write(f"**Historical Significance:** {info.get('historical_significance', 'N/A')}")
                    st.write(f"**Visual Elements:** {info.get('visual_elements', 'N/A')}")
                    st.write(f"**Confidence:** {info.get('confidence', 'N/A')}")
                
                # Display image gallery
                if st.session_state.landmark_images:
                    st.markdown("### 🖼️ Image Gallery")
                    cols = st.columns(3)
                    for idx, img in enumerate(st.session_state.landmark_images[:3]):
                        with cols[idx]:
                            st.image(img['url'], caption=img.get('caption', ''), use_container_width=True)
    
    # Right Column - Conversation
    with col_right:
        st.markdown("### 💬 Conversation with History")
        
        # Check if we need monument clarification
        if st.session_state.get('needs_monument_clarification', False):
            st.markdown("""
            <div class="persona-card">
                <div class="persona-avatar">📜</div>
                <div class="persona-name">Ancient Historian</div>
                <div class="persona-title">Keeper of History</div>
                <div class="persona-era">⏳ Timeless</div>
                <div class="persona-connection">"I could not clearly identify this monument from the image. Please help me understand which historical place you wish to explore."</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Show what was detected (if anything)
            if st.session_state.get('partial_visual_info'):
                st.info(f"🔍 I can see: {st.session_state.partial_visual_info}")
            
            # Ask user to clarify
            clarification_input = st.text_input(
                "Which monument is this?",
                placeholder="Enter the monument name..."
            )
            
            if clarification_input and st.button("✨ Continue Journey", use_container_width=True):
                # Use the clarified name to research and continue
                generator = PersonaGenerator(st.session_state.api_key, st.session_state.selected_model)
                
                with st.spinner("🔍 Researching monument..."):
                    landmark_info = generator.research_monument(clarification_input)
                    st.session_state.landmark_info = landmark_info
                
                with st.spinner("👻 Summoning historical figure..."):
                    persona = generator.generate_persona(landmark_info)
                    st.session_state.current_persona = persona
                    related = generator.generate_related_personas(landmark_info, persona)
                    st.session_state.related_personas = related
                
                with st.spinner("🖼️ Gathering monument images..."):
                    fetcher = WikipediaFetcher()
                    images = fetcher.fetch_images(
                        landmark_info.get('landmark_name', clarification_input),
                        config.WIKIPEDIA_IMAGE_COUNT
                    )
                    st.session_state.landmark_images = images
                
                # Clear clarification flag
                st.session_state.needs_monument_clarification = False
                st.session_state.partial_visual_info = None
                st.session_state.chat_history = []
                st.session_state.greeted = False
                st.rerun()
        
        elif not st.session_state.current_persona:
            # Welcome section
            st.markdown("""
            <div class="welcome-section">
                <div class="welcome-title">🌟 Welcome, Time Traveler!</div>
                <div class="welcome-text">
                    Embark on an extraordinary journey through time. Upload a photo of any historical monument, 
                    and we'll summon the spirits of those who built, designed, or lived in these magnificent places.
                </div>
                <div class="feature-box">
                    <strong>✨ What You Can Do:</strong><br>
                    • Upload photos of monuments like the Taj Mahal, Colosseum, Pyramids, etc.<br>
                    • Meet AI-generated historical personas who bring stories to life<br>
                    • Ask questions and hear their personal accounts<br>
                    • Enable voice narration for an immersive experience<br>
                    • Activate cinematic mode for full-screen storytelling
                </div>
                <div class="welcome-text" style="margin-top: 1rem;">
                    <strong>Try these famous monuments:</strong><br>
                    Taj Mahal • Eiffel Tower • Great Wall of China • Colosseum • Machu Picchu
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Display persona card
            persona = st.session_state.current_persona
            st.markdown(f"""
            <div class="persona-card">
                <div class="persona-avatar">{persona.get('avatar', '🏛️')}</div>
                <div class="persona-name">{persona.get('name', 'Unknown')}</div>
                <div class="persona-title">{persona.get('title', '')}</div>
                <div class="persona-era">{persona.get('era', '')}</div>
                <div class="persona-connection">"{persona.get('connection', '')}"</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Generate greeting if not done yet
            if not st.session_state.greeted:
                with st.spinner("✍️ Preparing greeting..."):
                    try:
                        persona_gen = PersonaGenerator(st.session_state.api_key, st.session_state.selected_model)
                        greeting = persona_gen.generate_greeting(
                            st.session_state.current_persona,
                            st.session_state.landmark_info
                        )
                        
                        st.session_state.chat_history.append({
                            'role': 'assistant',
                            'content': greeting
                        })
                        st.session_state.greeted = True
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error generating greeting: {e}")
            
            # Chat history
            st.markdown("---")
            chat_container = st.container()
            
            with chat_container:
                for idx, message in enumerate(st.session_state.chat_history):
                    role = message['role']
                    content = message['content']
                    
                    if role == 'user':
                        st.markdown(f"""
                        <div class="chat-message user-message">
                            <strong>You:</strong><br>
                            {content}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="chat-message ai-message">
                            <strong>{persona.get('name', 'Guide')}:</strong><br>
                            {content}
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Generate and display audio if enabled
                        if st.session_state.audio_enabled and idx == len(st.session_state.chat_history) - 1:
                            try:
                                voice_gen = VoiceGenerator()
                                audio_base64 = voice_gen.generate_speech(
                                    content,
                                    st.session_state.current_persona
                                )
                                
                                if audio_base64:
                                    audio_html = voice_gen.get_audio_html(audio_base64, autoplay=False)
                                    st.markdown(audio_html, unsafe_allow_html=True)
                                    
                                    # Show immersive mode if enabled
                                    if st.session_state.immersive_mode and st.session_state.landmark_images:
                                        immersive = ImmersiveMode()
                                        immersive_html = immersive.generate_immersive_html(
                                            st.session_state.current_persona,
                                            content,
                                            st.session_state.landmark_images,
                                            audio_base64
                                        )
                                        components.html(immersive_html, height=800, scrolling=False)
                            except Exception as e:
                                st.warning(f"Could not generate audio: {e}")
            
            # Suggested questions
            if len(st.session_state.chat_history) <= 2:
                st.markdown("### 💡 Suggested Questions")
                suggestions = [
                    "Tell me about the day this monument was completed",
                    "What was daily life like during your time?",
                    "What inspired the design of this place?",
                    "What challenges did you face in building this?"
                ]
                
                cols = st.columns(2)
                for idx, suggestion in enumerate(suggestions):
                    with cols[idx % 2]:
                        if st.button(suggestion, key=f"suggestion_{idx}", use_container_width=True):
                            process_user_message(suggestion)
                            st.rerun()
            
            # Chat input
            st.markdown("---")
            user_input = st.chat_input("Ask your historical guide anything...")
            
            if user_input:
                process_user_message(user_input)
                st.rerun()


if __name__ == "__main__":
    main()
