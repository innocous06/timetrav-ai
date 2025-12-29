# TimeTraveler AI 🏛️

**Where History Speaks Through Those Who Made It**

TimeTraveler AI is an immersive historical storytelling platform that brings monuments and landmarks to life through AI-generated historical personas. Upload a photo of any monument, and chat with the architects, builders, rulers, and historical figures who created these magnificent structures.

![TimeTraveler AI](https://img.shields.io/badge/Powered%20by-Google%20Gemini-4285F4?style=for-the-badge&logo=google)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.41.0-FF4B4B?style=for-the-badge&logo=streamlit)

---

## ✨ Features

### 🔍 **Intelligent Monument Recognition**
- Upload photos of any historical monument or landmark
- Powered by Google Gemini 2.0 Flash AI for accurate identification
- Extracts detailed information: name, location, era, architectural style, and historical significance

### 🎭 **Dynamic Historical Personas**
- AI generates authentic historical figures connected to each monument
- Choose from multiple personas: architects, builders, rulers, artisans
- Each persona has unique personality, speaking style, and historical knowledge
- Stay in character with period-appropriate language and perspectives

### 💬 **Interactive Conversations**
- Chat naturally with historical figures in real-time
- Ask about construction techniques, daily life, inspirations, and challenges
- Get personal stories and anecdotes from those who lived it
- Context-aware responses based on conversation history

### 🔊 **Voice Narration**
- Text-to-speech powered by gTTS
- Region-appropriate voice selection (French for French monuments, etc.)
- Optional auto-play for immersive experience

### 🎬 **Cinematic Immersive Mode**
- Full-screen experience with image slideshows
- Animated audio visualizers
- Elegant subtitle display
- Auto-advancing photo gallery from Wikipedia
- Keyboard navigation support

### 🖼️ **Image Galleries**
- Automatically fetches related images from Wikipedia
- Beautiful thumbnail displays
- Multiple views of each monument

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/innocous06/timetrav-ai.git
   cd timetrav-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your free Google Gemini API key**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy your API key

4. **Configure your API key**
   
   Option A - Environment Variable (Recommended):
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```
   
   Option B - Enter in App:
   - Leave .env empty and enter the key in the sidebar when the app starts

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in your terminal

---

## 📖 How to Use

### Step 1: Upload a Monument Photo
1. Take or find a clear photo of any historical monument
2. Use the file uploader on the left side
3. Supported formats: JPG, JPEG, PNG

### Step 2: Identify & Summon Guide
1. Click the "🔍 Identify & Summon Historical Guide" button
2. Wait while AI analyzes the monument (~5-10 seconds)
3. A historical persona will be generated

### Step 3: Chat with History
1. Read the persona's greeting
2. Use suggested questions or type your own
3. Explore different aspects of history
4. Switch between different personas using sidebar buttons

### Step 4: Enhance Your Experience
- **Enable Voice Narration**: Toggle in sidebar for audio responses
- **Activate Immersive Mode**: Full-screen cinematic experience
- **Explore Image Gallery**: View multiple photos of the monument
- **Try Different Personas**: Switch to hear different perspectives

---

## ⚙️ Configuration

### Environment Variables (`.env`)
```bash
GOOGLE_API_KEY=your_api_key_here
```

### Configuration Options (`config.py`)
- `GEMINI_MODEL`: AI model to use (default: "gemini-2.0-flash")
- `MAX_IMAGE_SIZE`: Maximum image dimensions (default: 1024x1024)
- `WIKIPEDIA_IMAGE_COUNT`: Number of images to fetch (default: 5)
- `DEFAULT_VOICE_LANG`: Default voice language (default: "en")
- `VOICE_SLOW`: Slow down speech (default: False)

---

## 🎯 Example Monuments to Try

### Famous Landmarks
- **Taj Mahal** (India) - Meet Shah Jahan or Ustad Ahmad Lahori
- **Eiffel Tower** (France) - Chat with Gustave Eiffel
- **Colosseum** (Italy) - Speak with Emperor Vespasian
- **Great Wall of China** - Meet Emperor Qin Shi Huang
- **Pyramids of Giza** (Egypt) - Talk to Pharaoh Khufu

### Ancient Wonders
- Parthenon (Greece)
- Machu Picchu (Peru)
- Angkor Wat (Cambodia)
- Petra (Jordan)
- Stonehenge (UK)

### Modern Marvels
- Statue of Liberty (USA)
- Sydney Opera House (Australia)
- Burj Khalifa (UAE)
- Golden Gate Bridge (USA)

---

## 🛠️ Technical Stack

### Core Technologies
- **[Streamlit](https://streamlit.io/)** 1.41.0 - Web application framework
- **[Google GenAI SDK](https://pypi.org/project/google-genai/)** 1.56.0 - AI/ML capabilities (NEW SDK)
- **[gTTS](https://github.com/pndurette/gTTS)** 2.5.4 - Text-to-speech
- **[Pillow](https://python-pillow.org/)** 11.0.0 - Image processing
- **[Requests](https://requests.readthedocs.io/)** 2.32.3 - HTTP library
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** 4.12.3 - HTML parsing

### AI Models
- **Gemini 2.0 Flash** - Fast, efficient multimodal AI
  - Image analysis and monument identification
  - Natural language conversation generation
  - Historical persona creation

### APIs Used
- **Google Gemini API** - Core AI functionality
- **Wikipedia API** - Monument images and information
- **Picsum Photos** - Fallback placeholder images

---

## 📁 Project Structure

```
timetrav-ai/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── config.py                 # Configuration settings
├── styles.py                 # Custom CSS styles
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore file
├── README.md                 # This file
└── utils/
    ├── __init__.py           # Package exports
    ├── image_analyzer.py     # Monument image analysis with Gemini
    ├── persona_generator.py  # Historical persona creation
    ├── wikipedia_fetcher.py  # Fetch monument images from Wikipedia
    ├── voice_generator.py    # Text-to-speech with gTTS
    └── immersive_mode.py     # Cinematic display component
```

---

## 🐛 Troubleshooting

### API Key Issues
**Problem**: "API Key Required" warning
- **Solution**: Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- Add it to `.env` file or enter in sidebar

### Image Upload Issues
**Problem**: Upload fails or image not recognized
- **Solution**: 
  - Ensure image is clear and monument is visible
  - Use JPG, JPEG, or PNG format
  - Keep file size under 10MB
  - Try a different photo angle

### No Audio Playing
**Problem**: Voice narration doesn't work
- **Solution**:
  - Check "Enable voice narration" in sidebar
  - Ensure browser allows audio playback
  - Try clicking the audio player controls
  - Check browser console for errors

### Wikipedia Images Not Loading
**Problem**: Gallery shows placeholder images
- **Solution**:
  - Check internet connection
  - Monument name may not have Wikipedia article
  - Try uploading a different monument photo
  - Placeholders still provide visual experience

### Slow Response Times
**Problem**: AI responses take too long
- **Solution**:
  - Check internet connection speed
  - Google Gemini API may have temporary slowdowns
  - Try refreshing the page
  - Consider upgrading to Gemini API paid tier for faster responses

---

## 🔐 Privacy & Security

- **API Keys**: Never commit `.env` file to version control
- **Images**: Uploaded images are processed in memory, not stored permanently
- **Conversations**: Chat history exists only in browser session
- **Data**: No user data is collected or stored on external servers

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Ideas for Contributions
- Add support for more languages
- Improve persona personalities
- Add more historical context
- Enhance UI/UX design
- Add unit tests
- Optimize performance
- Add more monument databases

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- **Google Gemini Team** - For the powerful AI API
- **Streamlit Team** - For the amazing web framework
- **Wikipedia** - For providing monument images and information
- **gTTS Contributors** - For text-to-speech capabilities
- **Historical Figures** - For inspiring this journey through time

---

## 📧 Contact & Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/innocous06/timetrav-ai/issues)
- **Discussions**: [Join the conversation](https://github.com/innocous06/timetrav-ai/discussions)

---

## 🌟 Example Conversations

### With Shah Jahan at the Taj Mahal
```
You: Why did you build the Taj Mahal?

Shah Jahan: Ah, my heart still aches at the memory. The Taj Mahal 
is my eternal tribute to my beloved wife, Mumtaz Mahal, who left 
this world too soon. Every white marble stone, every intricate 
carving, every precious gem inlaid - all speak of a love that 
transcends death itself. I wanted to create something that would 
stand through the ages as a testament to our bond.
```

### With Gustave Eiffel at the Eiffel Tower
```
You: What challenges did you face building the tower?

Gustave Eiffel: Mon ami, the criticism was relentless! Parisian 
artists and intellectuals called my iron tower a "metal monstrosity" 
and petitioned to stop construction. But I had faith in my 
engineering and vision. The real challenge was the wind - we had 
to account for every gust that would push against those iron girders. 
Yet here she stands, graceful and strong!
```

---

## 🎬 Screenshots

*Upload your monument photo and experience history come alive!*

---

**Made with ❤️ and powered by AI** | **Start your journey through time today!** 🚀
