import streamlit as st 
import json,requests
from pprint import pprint

keyword=st.text_input('plz give me a keyword: ')

option = st.selectbox(
     'Please choose an option: ',
     ('rel_syn', 'rel_ant', 'sl', 'ml', 'sd'))

st.write('You selected:', option)


                                                   
url= 'https://api.datamuse.com/words?' + option + '=' + keyword + '&max=10'

st.write("Here is the url: ", url)

response = requests.get(url)   

dataFromDatamuse = json.loads(response.text) 

for e in dataFromDatamuse:
  print(e['word'])


#st.write(dataFromDatamuse)

