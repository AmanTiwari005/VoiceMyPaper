# Research Paper to Podcast Converter 🎙️

This Streamlit application converts research paper PDFs into engaging podcasts. It extracts text from PDFs, summarizes the content, and generates speech audio. Optionally, the voice tone can be adjusted based on sentiment analysis, and background music can be added for a richer auditory experience.

## Features

- Extract text from PDF files
- Summarize the content of PDFs
- Analyze sentiment of the text
- Convert text to speech using gTTS
- Add background music to the generated podcast
- Utilize the GROQ model for summarization

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/research-paper-to-podcast.git
    cd research-paper-to-podcast
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables by creating a `.env` file and adding your GROQ API key:

    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Upload your PDF document using the sidebar and choose your settings.

3. Click "Generate Podcast" to create your podcast.

## Code Overview

### Main Application

The main application is contained in `app.py` and includes:

- `init_groq_model`: Initializes the GROQ model for summarization.
- `extract_text_from_pdf`: Extracts text from PDF files.
- `chunk_text`: Splits text into manageable chunks.
- `summarize_text`: Summarizes the text using the GROQ model.
- `analyze_sentiment`: Analyzes the sentiment of the text using TextBlob.
- `text_to_speech_gtts`: Converts text to speech using gTTS, with optional sentiment-based voice adjustment.
- `merge_audio_with_background`: Merges the generated speech audio with background music.
- Streamlit layout and user interactions.

### Additional Files

- `requirements.txt`: Lists all the dependencies needed for the project.
- `.env`: Contains the environment variables, specifically the GROQ API key.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [HuggingFace](https://huggingface.co/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [gTTS](https://pypi.org/project/gTTS/)
- [pydub](https://pypi.org/project/pydub/)
- [GROQ](https://groq.com/)

Feel free to fork this repository and customize it to suit your needs. Contributions are welcome!
