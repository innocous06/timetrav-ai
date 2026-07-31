# timetrav-ai

A Streamlit application that identifies historical monuments from uploaded photos and generates AI-driven historical personas to converse with. Powered by Google Gemini for image analysis and natural language generation.

## Requirements

- Python 3.8+
- Google Gemini API key (free tier available at [aistudio.google.com](https://aistudio.google.com/app/apikey))

## Installation

```sh
git clone https://github.com/innocous06/timetrav-ai.git
cd timetrav-ai
pip install -r requirements.txt
```

## Configuration

Copy the environment template and add your API key:

```sh
cp .env.example .env
```

Edit `.env`:

```
GOOGLE_API_KEY=your_api_key_here
```

Alternatively, enter the key directly in the app sidebar when it starts.

## Usage

```sh
streamlit run app.py
```

Open `http://localhost:8501` in your browser. Upload a photo of any historical monument to begin.

## License

MIT License

Copyright (c) 2024 innocous06

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
