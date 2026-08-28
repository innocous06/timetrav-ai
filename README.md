# timetrav-ai

[![Language: Python](https://img.shields.io/badge/language-Python_3.9+-18181f?style=flat-square)](https://www.python.org/)
[![Framework: Streamlit](https://img.shields.io/badge/framework-Streamlit-18181f?style=flat-square)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/license-MIT-18181f?style=flat-square)](LICENSE)

An interactive multimodal AI platform that identifies historical monuments and landmarks from uploaded images and generates dynamic, conversational historical personas to interact with.

## Overview

timetrav-ai combines computer vision and large language models to transform static historical education into an interactive experience. Users upload an image of any historical monument, and the platform recognizes the landmark, retrieves verified historical context, synthesizes an authentic historical persona from that era, and facilitates real-time dialogue.

## Key Capabilities

- Automated visual landmark and monument recognition using multimodal vision models.
- Dynamic persona generation calibrated with historical speech patterns, era-specific knowledge, and verified contextual data.
- Automated retrieval and cross-verification of historical facts via Wikipedia knowledge integration.
- Custom responsive dark-mode interface built on Streamlit with immersive storytelling elements.

## Tech Stack

- **Language:** Python 3.9+
- **AI & LLM Services:** Google Gemini Vision & LLM APIs
- **Frontend & UI:** Streamlit, Custom CSS Styling Components
- **Data & Verification:** Wikipedia API, Python Imaging Library (PIL), Requests
- **Configuration:** Python-dotenv, Session State Management

## Usage

```bash
# Clone and install dependencies
git clone https://github.com/innocous06/timetrav-ai.git
cd timetrav-ai
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Add your GEMINI_API_KEY in .env

# Launch application
streamlit run app.py
```

## Persona Synthesis Pipeline

1. **Vision Inference:** Google Gemini multimodal vision model processes landmark imagery to extract architectonic style, historical epoch, and geographic location.
2. **Knowledge Retrieval:** Wikipedia API fetches verified historical chronology and figures associated with the monument.
3. **Dialogue Calibration:** Dynamic system prompts instantiate conversational historical personas with authentic vocabulary and perspective.

## License

Released under the [MIT License](LICENSE).

Copyright (c) 2026 innocous06. All rights reserved.
