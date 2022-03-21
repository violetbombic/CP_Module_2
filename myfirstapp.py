import streamlit as st
st.text("hello world")

st.header("hello world")  
st.text("from Brixen")  


title = st.text_input('Gimme a movie title', '<enter a movie title here>')
st.write('The current movie title is', title)
