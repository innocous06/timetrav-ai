"""
Custom CSS styles for TimeTraveler AI application
"""

def get_custom_css():
    return """
    <style>
    /* Main app background with dark gradient */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #e8e8e8;
    }
    
    /* Animated header with shimmer effect */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #ff6b6b);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 4s ease infinite;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0;
    }
    
    @keyframes shimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .subtitle {
        text-align: center;
        color: #b8b8b8;
        font-size: 1.2rem;
        margin-top: -1rem;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    /* Persona card styling */
    .persona-card {
        background: linear-gradient(135deg, rgba(78, 205, 196, 0.1) 0%, rgba(69, 183, 209, 0.1) 100%);
        border: 2px solid #4ecdc4;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(78, 205, 196, 0.2);
        backdrop-filter: blur(10px);
    }
    
    .persona-avatar {
        font-size: 4rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .persona-name {
        font-size: 2rem;
        font-weight: bold;
        color: #4ecdc4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .persona-title {
        font-size: 1.2rem;
        color: #45b7d1;
        text-align: center;
        margin-bottom: 0.5rem;
        font-style: italic;
    }
    
    .persona-era {
        font-size: 1rem;
        color: #b8b8b8;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .persona-connection {
        font-size: 0.95rem;
        color: #e8e8e8;
        text-align: center;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        font-style: italic;
    }
    
    /* Chat message bubbles */
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 15px;
        max-width: 80%;
        animation: fadeIn 0.3s ease;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: auto;
        margin-right: 0;
        text-align: right;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .ai-message {
        background: linear-gradient(135deg, rgba(78, 205, 196, 0.2) 0%, rgba(69, 183, 209, 0.2) 100%);
        border: 1px solid rgba(78, 205, 196, 0.3);
        color: #e8e8e8;
        margin-right: auto;
        margin-left: 0;
        box-shadow: 0 4px 15px rgba(78, 205, 196, 0.2);
    }
    
    /* Styled buttons */
    .stButton > button {
        background: linear-gradient(135deg, #4ecdc4 0%, #45b7d1 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(78, 205, 196, 0.4);
        background: linear-gradient(135deg, #45b7d1 0%, #4ecdc4 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Secondary buttons (like related personas) */
    .secondary-button {
        background: linear-gradient(135deg, rgba(255, 107, 107, 0.8) 0%, rgba(255, 107, 107, 0.6) 100%) !important;
        border: 1px solid #ff6b6b !important;
    }
    
    /* Welcome section */
    .welcome-section {
        background: linear-gradient(135deg, rgba(255, 107, 107, 0.1) 0%, rgba(78, 205, 196, 0.1) 100%);
        border: 2px solid rgba(78, 205, 196, 0.3);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
    }
    
    .welcome-title {
        font-size: 2rem;
        color: #4ecdc4;
        margin-bottom: 1rem;
    }
    
    .welcome-text {
        font-size: 1.1rem;
        color: #e8e8e8;
        line-height: 1.8;
        margin-bottom: 1.5rem;
    }
    
    .feature-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Info box styling */
    .info-box {
        background: linear-gradient(135deg, rgba(69, 183, 209, 0.1) 0%, rgba(78, 205, 196, 0.1) 100%);
        border-left: 4px solid #4ecdc4;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    
    /* Landmark info display */
    .landmark-info {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .landmark-name {
        font-size: 1.8rem;
        color: #4ecdc4;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .landmark-detail {
        font-size: 1rem;
        color: #b8b8b8;
        margin: 0.3rem 0;
    }
    
    /* Audio player styling */
    audio {
        width: 100%;
        margin: 0.5rem 0;
        border-radius: 10px;
    }
    
    /* Image gallery */
    .image-gallery {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    
    /* Suggested questions */
    .suggested-question {
        background: rgba(78, 205, 196, 0.1);
        border: 1px solid #4ecdc4;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        margin: 0.5rem;
        display: inline-block;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .suggested-question:hover {
        background: rgba(78, 205, 196, 0.2);
        transform: translateY(-2px);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #0f3460 100%);
    }
    
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        margin: 0.5rem 0;
    }
    
    /* File uploader */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Text input */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(78, 205, 196, 0.3);
        border-radius: 10px;
    }
    
    /* Chat input */
    .stChatInput > div > div > textarea {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(78, 205, 196, 0.3);
        border-radius: 10px;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(78, 205, 196, 0.1);
        border-radius: 10px;
        color: #4ecdc4 !important;
    }
    
    /* Success/Info/Warning messages */
    .stSuccess, .stInfo, .stWarning {
        border-radius: 10px;
    }
    
    /* Column borders for visual separation */
    [data-testid="column"] {
        border-radius: 10px;
        padding: 1rem;
    }
    </style>
    """
