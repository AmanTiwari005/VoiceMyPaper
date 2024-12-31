import streamlit as st
import PyPDF2
from transformers import pipeline
from textblob import TextBlob
from gtts import gTTS
from pydub import AudioSegment

# Set the path to the FFmpeg executable
AudioSegment.converter = r"C:/FFmpeg/ffmpeg.exe"

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        st.error(f"Failed to extract text from PDF: {e}")
        return ""

def chunk_text(text, max_chunk_length=512):
    words = text.split()
    for i in range(0, len(words), max_chunk_length):
        yield ' '.join(words[i:i + max_chunk_length])

def summarize_text(text, max_length=150):
    summarizer = pipeline("summarization")
    summary = ""
    
    for chunk in chunk_text(text):
        chunk = chunk.strip()
        if len(chunk) == 0 or len(chunk.split()) < 5:
            continue

        try:
            chunk_summary = summarizer(chunk, max_length=max_length, min_length=50, do_sample=False)
            if isinstance(chunk_summary, list) and len(chunk_summary) > 0:
                summary += chunk_summary[0]['summary_text'] + " "
            else:
                st.warning("No summary produced for chunk.")
        except Exception as e:
            st.error(f"Error summarizing chunk: {e}")

    return summary.strip()

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def text_to_speech_gtts(text, sentiment_adjustment=False):
    if sentiment_adjustment:
        sentiment = analyze_sentiment(text)
        speech_rate = 1.0 if sentiment > 0 else 0.9
    else:
        speech_rate = 1.0

    # # Save audio to a temporary file
    # with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
    #     tts = gTTS(text=text, lang='en', slow=False)
    #     tts.save(tmp_file.name)  # Save the audio to the temp file
    #     return tmp_file.name  # Return the path to the saved audio file

def merge_audio_with_background(audio_file_path, background_music):
    if not audio_file_path:
        raise ValueError("Audio file path must be provided.")
    if not background_music:
        raise ValueError("Background music file must be uploaded.")

    st.write(f"Merging audio: {audio_file_path} with background: {background_music}")

    # Read the audio file directly from the file path
    speech = AudioSegment.from_file(audio_file_path, format="mp3")

    # Read the background music from the file path
    background = AudioSegment.from_file(background_music, format="mp3")

    # Overlay the two audio segments
    combined = speech.overlay(background)

    # Save the combined audio to a new file
    combined_audio_path = "combined_podcast.mp3"
    combined.export(combined_audio_path, format="mp3")

    return combined_audio_path


# Streamlit application layout
st.title("Research Paper to Podcast Converter 🎙️")
st.write("Upload a research paper PDF, and we'll generate a podcast for you!")

uploaded_pdf = st.file_uploader("Choose a PDF file", type="pdf")
background_music = st.file_uploader("Upload background music (Optional)", type=["mp3"])
summarize = st.checkbox("Summarize the paper")
sentiment_adjustment = st.checkbox("Adjust voice tone based on sentiment")

if st.button("Generate Podcast"):
    if uploaded_pdf is not None:
        with st.spinner("Extracting text from PDF..."):
            pdf_text = extract_text_from_pdf(uploaded_pdf)

        if summarize:
            with st.spinner("Summarizing the content..."):
                pdf_text = summarize_text(pdf_text)

        with st.spinner("Generating podcast..."):
            audio_file_path = text_to_speech_gtts(pdf_text, sentiment_adjustment=sentiment_adjustment)
        st.write(f"Generated audio file path: {audio_file_path}")  # Debug check

        # Handle background music if uploaded
        if background_music:
            # Save background music to a file
            background_music_path = "background_music.mp3"
            with open(background_music_path, "wb") as f:
                f.write(background_music.read())
            st.write(f"Background music file saved at: {background_music_path}")  # Debug check

            # Merge the audio with background music
            with st.spinner("Merging audio with background music..."):
                podcast_file = merge_audio_with_background(audio_file_path, background_music_path)
            st.success(f"Podcast generated with background music as {podcast_file}")
            st.audio(podcast_file)
        else:
            st.success(f"Podcast generated as {audio_file_path}")
            st.audio(audio_file_path)
