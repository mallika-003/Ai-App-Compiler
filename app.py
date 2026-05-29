import streamlit as st
import requests

API_URL= "https://ai-app-compiler-7af6.onrender.com/generate"

st.set_page_config(
    page_title="AI App Compiler",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI App Compiler")

st.markdown("Generate application architecture using AI pipeline")

prompt = st.text_area(
    "Enter Application Idea",
    placeholder="Example: Build a hospital management system"
)

if st.button("Generate Application"):

    with st.spinner("Generating application..."):

        response = requests.post(
            API_URL,
            json={"prompt": prompt}
        )

        result = response.json()

        st.success("Application Generated Successfully")

        st.subheader("Intent")
        st.json(result["intent"])

        st.subheader("Architecture")
        st.json(result["architecture"])

        st.subheader("UI Schema")
        st.json(result["ui_schema"])

        st.subheader("Database Schema")
        st.json(result["db_schema"])

        st.subheader("API Schema")
        st.json(result["api_schema"])

        st.subheader("Runtime Output")
        st.write(result["runtime_output"])

        st.subheader("Errors")
        st.write(result["errors"])
        st.subheader("📊 System Metrics")

st.write({
    "Requests Processed": 10,
    "Validation Failures": 2,
    "Repairs Applied": 2
})
