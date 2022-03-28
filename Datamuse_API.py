import streamlit as st 
import json,requests
from pprint import pprint

keyword=input('plz give me a keyword: ')

option = st.selectbox(
     'How would you like to be contacted?',
     ('rel_syn', 'rel_ant', 'sl', 'ml', 'sd'))

st.write('You selected:', option)


                                                   
url= 'https://api.datamuse.com/words?' + option + '=' + keyword + '&max=10'

st.write(url)

# response = requests.get(url)   

# dataFromDatamuse = json.loads(response.text) 

# st.write(dataFromDatamuse)

