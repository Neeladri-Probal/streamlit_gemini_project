from google import genai
from dotenv import load_dotenv
import os
import io
from gtts import gTTS
import streamlit as st
#loading the environment variable
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")
#initializing a client
client = genai.Client(api_key=my_api_key)
#note generator
def note_generator(images):
    prompth = """Summarize the picture in note format at max 100 words, make sure to add neccessary markdown to differentiate different section"""
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images,prompth]
    )
    return response.text
def audio_transcription(text):
    speech = gTTS(text)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer
def quiz_generator(images,difficulty):
    prompth = f"""Generate 3 quizzes based on {difficulty}.Make sure to add markdown to differentiate the options"""
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images,prompth]
    )
    return response.text