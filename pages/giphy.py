import streamlit as st
import requests

url = 'https://api.giphy.com/v1/gifs/search'

api_key = st.secrets.GIPHY_KEY.api_key_2

query = st.text_input('Choose the gif you would like to see.', value='dog')

params = {'api_key':api_key,
          'q': query}

response = requests.get(url, params=params).json()

giphy = response['data'][0]['embed_url']

st.write(giphy)

st.write(f"<iframe src={giphy} >", unsafe_allow_html=True)
