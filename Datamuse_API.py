import streamlit as st 
import json, request
from pprint import pprint



keyword=st.text_input('plz give me a keyword: ')

option = st.selectbox(
     'Please choose an option: ',
     ('Synonymes', 'Antonyms', 'Sounds Like', 'Means Like', 'Spelled Like'))

st.write('You selected:', option)

if option == 'Synonymes':
     url= 'https://api.datamuse.com/words?rel_syn=' + keyword + '&max=10'
elif option == 'Antonyms':
     url= 'https://api.datamuse.com/words?rel_ant=' + keyword + '&max=10'
elif option == 'Sounds Like':
     url= 'https://api.datamuse.com/words?sl=' + keyword + '&max=10'
elif option == 'Means Like':
     url= 'https://api.datamuse.com/words?ml=' + keyword + '&max=10'
else:
     url= 'https://api.datamuse.com/words?sd=' + keyword + '&max=10'
     

                                                   
#url= 'https://api.datamuse.com/words?' + option + '=' + keyword + '&max=10'

st.write("Here is the url: ", url)

response = requests.get(url)   

dataFromDatamuse = json.loads(response.text) 

sr.write("You chose: ", keyword, ". And the result of", option, "is: ")
     
for eachentry in dataFromDatamuse:
  st.write("--",eachentry['word'])


#st.write(dataFromDatamuse)

