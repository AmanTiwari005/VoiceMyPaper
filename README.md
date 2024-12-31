# Research Paper to Podcast Converter 🎙️

This project provides a tool to convert research papers (in PDF format) into audio podcasts. The app extracts text from a PDF, optionally summarizes it, converts it into speech, and allows you to add background music to the generated podcast.

## Features

- **PDF Text Extraction**: Upload a research paper in PDF format, and the text will be extracted for further processing.
- **Text Summarization**: Optionally summarize the content of the research paper to shorten the audio.
- **Text-to-Speech Conversion**: Converts the extracted text into speech using Google TTS (gTTS).
- **Sentiment-Based Voice Adjustment**: Adjusts the speech tone based on sentiment analysis of the text.
- **Background Music**: Merge generated speech with your background music (optional).

## Requirements

- Python 3.7+
- Streamlit
- PyPDF2
- Transformers (for GPT models)
- TextBlob
- gTTS (Google Text-to-Speech)
- pydub (for audio manipulation)
- langchain_groq (for integrating ChatGroq)
- dotenv (for loading environment variables)
- FFmpeg (for audio file manipulation)

## Setup

1. **Clone this repository**:

   ```bash
   git clone https://github.com/yourusername/research-paper-to-podcast.git
   cd research-paper-to-podcast
