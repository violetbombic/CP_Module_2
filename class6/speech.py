import streamlit as st
from gtts import gTTS
import IPython.display as ipd  

tts1=gTTS(text='hello world', lang='it')
tts1.save('helloworld_italian.mp3')

audio_file = open("audio.mp3", "rb")
st.write("you can listen to the audio here")

st.audio(data=audio_file, format="audio/mp3", start_time=0)
