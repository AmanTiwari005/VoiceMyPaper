# 🎙️ ResearchPod: Research Paper to Podcast Converter

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30.0-FF4B4B)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-LLaMa--3.1--70B-green)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Overview

ResearchPod is a powerful tool that converts academic research papers into engaging audio podcasts. Simply upload your PDF, add optional background music, and transform complex research into an accessible audio format. Perfect for researchers, students, and lifelong learners who prefer audio learning.

![ResearchPod Demo](https://raw.githubusercontent.com/yourusername/researchpod/main/demo.png)

## ✨ Features

- 📄 **PDF Processing**: Extract text from any research paper PDF
- 🧠 **AI Summarization**: Condense lengthy papers into concise summaries using LLaMa 3.1
- 🎵 **Background Music**: Add background music to enhance listening experience
- 😀 **Sentiment Analysis**: Adjust voice tone based on content sentiment
- 🔊 **Text-to-Speech**: Convert text to natural-sounding speech
- 🎧 **Audio Mixing**: Professionally merge speech with background music

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/researchpod.git
cd researchpod

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install FFmpeg (required for audio processing)
# Windows: Download from https://ffmpeg.org/download.html and update path in code
# Mac: brew install ffmpeg
# Linux: apt-get install ffmpeg
```

## 🔑 Environment Setup

1. Create a `.env` file in the project root
2. Add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

3. Make sure FFmpeg is properly installed and configured:
   - For Windows users: Update the path in the code to point to your FFmpeg executable
   - For Mac/Linux users: Ensure FFmpeg is installed and available in your PATH

## 🚀 Usage

```bash
streamlit run app.py
```

Then open your browser and navigate to `http://localhost:8501`

### How to use:
1. Upload a research paper PDF
2. Optionally upload background music (MP3 format)
3. Choose whether to summarize the paper
4. Select whether to adjust voice tone based on sentiment
5. Click "Generate Podcast" and enjoy your audio content!

## 📋 Requirements

- Python 3.8+
- Streamlit
- PyPDF2
- Transformers
- TextBlob
- gTTS (Google Text-to-Speech)
- pydub (with FFmpeg)
- LangChain
- Groq API access

## 🔄 How It Works

1. **Text Extraction**: Extract text content from the uploaded PDF
2. **Summarization**: (Optional) Summarize the content using LLaMa 3.1 model
3. **Sentiment Analysis**: (Optional) Analyze the text sentiment to adjust speech parameters
4. **Text-to-Speech Conversion**: Convert text to speech using Google's TTS engine
5. **Audio Mixing**: Combine speech with background music if provided
6. **Playback**: Stream the final audio directly in the browser

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/) for the web application framework
- [Groq](https://groq.com/) for the LLM API
- [Google Text-to-Speech](https://cloud.google.com/text-to-speech) for TTS functionality
- [pydub](https://github.com/jiaaro/pydub) for audio processing
- [PyPDF2](https://pythonhosted.org/PyPDF2/) for PDF processing
- [FFmpeg](https://ffmpeg.org/) for audio conversion

---

Made with ❤️ by Aman Tiwari
