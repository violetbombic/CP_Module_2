import streamlit as st
from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator

tts1=gTTS(text='hello world', lang='it')
tts1.save('audio.mp3')

audio_file = open("audio.mp3", "rb")
st.write("you can listen to the audio here")

st.audio(data=audio_file, format="audio/mp3", start_time=0)



text_by_user = st.text_input("Please type in some text here: ")
lang_code = st.text_input("Please type in 2-letter language code, for example: 'en' for english, 'de' for german...").lower()

tts=gTTS(text= text_by_user, lang= lang_code)
tts.save(text_by_user + '.mp3')


st.audio(data=text_by_user, format="audio/wav", start_time=0)
