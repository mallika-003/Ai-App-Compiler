import streamlit as st
import requests

st.title("AI App Compiler")

prompt = st.text_area("Enter App Idea")

if st.button("Generate"):

    response = requests.post(
        "http://127.0.0.1:8000/generate",
        json={"prompt": prompt}
    )

    data = response.json()

    st.subheader("Intent")
    st.json(data["intent"])

    st.subheader("Architecture")
    st.json(data["architecture"])

    st.subheader("UI Schema")
    st.json(data["ui_schema"])

    st.subheader("Database Schema")
    st.json(data["db_schema"])

    st.subheader("API Schema")
    st.json(data["api_schema"])

    st.subheader("Runtime Output")
    st.json(data["runtime_output"])

    st.subheader("Errors")
    st.json(data["errors"])
    st.subheader("System Metrics")
    st.write({
    "Requests Processed": 10,
    "Validation Failures": 2,
    "Repairs": 2
})