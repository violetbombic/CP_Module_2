import streamlit as st
from gtts import gTTS
import IPython.display as ipd  

text_by_user = st.text_input("Please type in some text here: ")
lang_code = st.text_input("Please type in 2-letter language code, for example: 'en' for english, 'de' for german...").lower()

tts=gTTS(text= text_by_user, lang= lang_code)
tts.save(text_by_user + '.mp3')

audio_file = open(text_by_user + ".mp3", "rb")

st.audio(data=audio_file, format="audio/mp3", start_time=0)
