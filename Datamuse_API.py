import json,requests
from pprint import pprint
import streamlite as st 

#keyword=input('plz give me a keyword: ')
option = st.selectbox('What you want to choose?', ('rel_syn', 'rel_ant', 'sl’, 'ml'))
st.write('You selected:', option):
url= 'https://api.datamuse.com/words?rel_ant=' + keyword + '&max=10'

response = requests.get(url)   

dataFromDatamuse = json.loads(response.text) 

