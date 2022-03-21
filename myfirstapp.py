import streamlit as st
st.text("hello world")

st.header("hello world")  
st.text("from Brixen")  


title = st.text_input('Gimme a movie title', '<enter a movie title here>')
st.write('The current movie title is', title)


genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'), help = 'click on one of the options')
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
     
     
     
# ! python3
import json, requests 

# add your own APIkey
APIkey = '3616c9537549584295b22c956c6fcf8d'
location = 'london'

# check API documentation to see what structure of URL is needed to access the data
# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
# print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
# print(response.text)  


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
# print(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

st.text(weatherData['main']['temp_max']) 
# more???????????
