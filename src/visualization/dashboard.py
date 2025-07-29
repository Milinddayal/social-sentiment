# Paste minimal Streamlit app code:

import streamlit as st
import requests

st.title("Social Media Sentiment Analysis")

text = st.text_area("Enter text:")

if st.button("Analyze"):
    r = requests.post("http://localhost:8000/predict", json={"text": text})
    st.write(r.json())