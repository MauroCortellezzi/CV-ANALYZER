
# main.py
# Main entry point for the CV Analyzer Streamlit app.
# Handles user interface, file upload, and calls analysis functions.

import streamlit as st  # Streamlit for web UI
import os
from openai import OpenAI  # OpenAI API for LLM analysis
from dotenv import load_dotenv  # For loading environment variables
from utils import extract_text_from_pdf, extract_text_from_file  # Text extraction utilities
from ai_analysis import analyze_cv  # LLM-based CV analysis
from ui import show_title, show_sidebar, show_section_header, show_section_footer  # UI components


# Load environment variables from .env file
load_dotenv()


# Set Streamlit page configuration
st.set_page_config(page_title="CV Analyzer", page_icon="🤖", layout="centered")


# Show main UI sections
show_title()
show_sidebar()
show_section_header()




# Get OpenAI API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# File uploader for CV (PDF or TXT)
uploaded_file = st.file_uploader("upload your resume (PDF OR TXT)", type=["pdf", "txt"])
# Input for job role
job_role = st.text_input("Enter the job role you are applying for:")
# Optional job description input
job_description = st.text_area("Optional: Paste the job description here (Job Description)")

# Show footer section
show_section_footer()
# Button to trigger analysis
analyze = st.button("Analyze CV")



# Main analysis logic: runs when user clicks the button and uploads a file
if analyze and uploaded_file:
    try:
        # Extract text from uploaded file
        file_content = extract_text_from_file(uploaded_file)

        # Check if file is empty
        if not file_content.strip():
            st.error("The uploaded file is empty or could not be read.")
            st.stop()

        # Run LLM-based CV analysis
        result = analyze_cv(OPENAI_API_KEY, file_content, job_role, job_description)

        # Display results
        st.markdown("### Analysis results")
        st.markdown(result)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")