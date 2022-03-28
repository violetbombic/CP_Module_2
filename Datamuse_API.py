import streamlit as st 

option = st.selectbox(
     'How would you like to be contacted?',
     ('rel_syn', 'rel_ant', 'sl', 'ml', 'sd'))

st.write('You selected:', option)

