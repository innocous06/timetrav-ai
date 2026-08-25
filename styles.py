"""
Custom CSS styles for TimeTraveler AI application
"""

def get_custom_css():
    return """
    <style>
    /* Main app background with rich, deep gradient */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 40%, #2c1e3e 70%, #1e1333 100%);
        color: #f0f0f5;
    }
    
    /* Animated header with elegant gold-amber shimmer */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #f4a261, #e9c46a, #f4e285, #e9c46a, #f4a261);
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
        color: #c5c6d0;
        font-size: 1.2rem;
        margin-top: -1rem;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    /* Persona card with elegant amber and teal accents */
    .persona-card {
        background: linear-gradient(135deg, rgba(244, 162, 97, 0.08) 0%, rgba(94, 129, 172, 0.12) 100%);
        border: 2px solid #e9c46a;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(233, 196, 106, 0.25), 0 0 40px rgba(94, 129, 172, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .persona-avatar {
        font-size: 4rem;
        text-align: center;
        margin-bottom: 1rem;
        filter: drop-shadow(0 0 8px rgba(233, 196, 106, 0.4));
    }
    
    .persona-name {
        font-size: 2rem;
        font-weight: bold;
        color: #f4e285;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 10px rgba(244, 162, 97, 0.3);
    }
    
    .persona-title {
        font-size: 1.2rem;
        color: #a4bfd4;
        text-align: center;
        margin-bottom: 0.5rem;
        font-style: italic;
    }
    
    .persona-era {
        font-size: 1rem;
        color: #c5c6d0;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .persona-connection {
        font-size: 0.95rem;
        color: #e8eaed;
        text-align: center;
        padding: 1rem;
        background: rgba(94, 129, 172, 0.15);
        border-radius: 10px;
        font-style: italic;
        border-left: 3px solid rgba(233, 196, 106, 0.5);
    }
    
    /* Chat message bubbles with improved contrast */
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
        background: linear-gradient(135deg, #5e81ac 0%, #88c0d0 100%);
        color: #ffffff;
        margin-left: auto;
        margin-right: 0;
        text-align: right;
        box-shadow: 0 4px 15px rgba(94, 129, 172, 0.4);
    }
    
    .ai-message {
        background: linear-gradient(135deg, rgba(244, 162, 97, 0.15) 0%, rgba(233, 196, 106, 0.12) 100%);
        border: 1px solid rgba(233, 196, 106, 0.4);
        color: #f0f0f5;
        margin-right: auto;
        margin-left: 0;
        box-shadow: 0 4px 15px rgba(233, 196, 106, 0.2);
    }
    
    /* Styled buttons with warm tones */
    .stButton > button {
        background: linear-gradient(135deg, #e9c46a 0%, #f4a261 100%);
        color: #1a1f3a;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(233, 196, 106, 0.35);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(233, 196, 106, 0.5);
        background: linear-gradient(135deg, #f4e285 0%, #e9c46a 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Secondary buttons (like related personas) */
    .secondary-button {
        background: linear-gradient(135deg, rgba(136, 192, 208, 0.8) 0%, rgba(94, 129, 172, 0.7) 100%) !important;
        border: 1px solid #88c0d0 !important;
    }
    
    /* Welcome section with warm inviting colors */
    .welcome-section {
        background: linear-gradient(135deg, rgba(244, 162, 97, 0.08) 0%, rgba(94, 129, 172, 0.1) 100%);
        border: 2px solid rgba(233, 196, 106, 0.4);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
    }
    
    .welcome-title {
        font-size: 2rem;
        color: #f4e285;
        margin-bottom: 1rem;
        text-shadow: 0 2px 10px rgba(244, 162, 97, 0.3);
    }
    
    .welcome-text {
        font-size: 1.1rem;
        color: #e8eaed;
        line-height: 1.8;
        margin-bottom: 1.5rem;
    }
    
    .feature-box {
        background: rgba(94, 129, 172, 0.12);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 3px solid rgba(233, 196, 106, 0.5);
    }
    
    /* Info box styling */
    .info-box {
        background: linear-gradient(135deg, rgba(136, 192, 208, 0.1) 0%, rgba(94, 129, 172, 0.1) 100%);
        border-left: 4px solid #88c0d0;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    
    /* Landmark info display */
    .landmark-info {
        background: rgba(94, 129, 172, 0.1);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(233, 196, 106, 0.3);
    }
    
    .landmark-name {
        font-size: 1.8rem;
        color: #f4e285;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 10px rgba(244, 162, 97, 0.3);
    }
    
    .landmark-detail {
        font-size: 1rem;
        color: #c5c6d0;
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
        background: rgba(233, 196, 106, 0.12);
        border: 1px solid rgba(233, 196, 106, 0.4);
        border-radius: 20px;
        padding: 0.5rem 1rem;
        margin: 0.5rem;
        display: inline-block;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .suggested-question:hover {
        background: rgba(233, 196, 106, 0.2);
        transform: translateY(-2px);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Sidebar styling with deep elegant gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0e27 0%, #1a1f3a 50%, #1e1333 100%);
        border-right: 1px solid rgba(233, 196, 106, 0.2);
    }
    
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        margin: 0.5rem 0;
    }
    
    /* File uploader with amber accent */
    [data-testid="stFileUploader"] {
        background: rgba(94, 129, 172, 0.08);
        border: 1px solid rgba(233, 196, 106, 0.3);
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Text input with better contrast */
    .stTextInput > div > div > input {
        background: rgba(30, 35, 55, 0.8);
        color: #f0f0f5;
        border: 1px solid rgba(233, 196, 106, 0.4);
        border-radius: 10px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #e9c46a;
        box-shadow: 0 0 0 2px rgba(233, 196, 106, 0.2);
    }
    
    /* Chat input */
    .stChatInput > div > div > textarea {
        background: rgba(30, 35, 55, 0.8);
        color: #f0f0f5;
        border: 1px solid rgba(233, 196, 106, 0.4);
        border-radius: 10px;
    }
    
    .stChatInput > div > div > textarea:focus {
        border-color: #e9c46a;
        box-shadow: 0 0 0 2px rgba(233, 196, 106, 0.2);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(233, 196, 106, 0.12);
        border-radius: 10px;
        color: #f4e285 !important;
    }
    
    /* Success/Info/Warning messages with improved colors */
    .stSuccess {
        background: rgba(163, 190, 140, 0.15);
        border-left: 4px solid #a3be8c;
        border-radius: 10px;
    }
    
    .stInfo {
        background: rgba(136, 192, 208, 0.15);
        border-left: 4px solid #88c0d0;
        border-radius: 10px;
    }
    
    .stWarning {
        background: rgba(235, 203, 139, 0.15);
        border-left: 4px solid #ebcb8b;
        border-radius: 10px;
    }
    
    /* Column borders for visual separation */
    [data-testid="column"] {
        border-radius: 10px;
        padding: 1rem;
    }
    </style>
    """

/* Image Preview Transitions */
.stImage img { border-radius: 8px; transition: transform 0.2s ease; }
