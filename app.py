import streamlit as st
import requests

API_URL= "https://ai-app-compiler-7af6.onrender.com/generate"

st.title("AI App Compiler")

prompt = st.text_area("Enter your app idea")

if st.button("Generate"):

    with st.spinner("Generating..."):

        response = requests.post(
            API_URL,
            json={"prompt": prompt}
        )

        st.json(response.json())
