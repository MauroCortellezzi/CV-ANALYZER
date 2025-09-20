
# ui.py
# UI component functions for the CV Analyzer Streamlit app.

import streamlit as st


def show_title():
    """
    Displays the main title and welcome message for the app.
    """
    st.markdown("<h1 style='text-align: center;'>CV Analyzer 🤖</h1>", unsafe_allow_html=True)
    st.success("Welcome to the CV Analyzer! Upload your CV in PDF or TXT format and get insights using OpenAI's GPT-4 model.")


def show_sidebar():
    """
    Displays the sidebar with instructions and branding.
    """
    st.sidebar.title("CV Analyzer")
    st.sidebar.markdown(
        "🚀 **Boost Your Job Search**\n\n"
        "Transform your resume into a powerful tool:\n"
        "- Upload your CV (PDF or TXT)\n"
        "- Enter your target job role\n"
        "- (Optional) Paste the job description\n"
        "- Click 'Analyze CV'\n\n"
        "Get personalized recommendations to stand out and better align your profile with your dream position."
    )
    st.sidebar.markdown("---")


def show_section_header():
    """
    Displays the section header for the main content area.
    """
    st.markdown("<h2 style='text-align: center;'>Analyze Your Resume Like a Pro 💡</h2>", unsafe_allow_html=True)


def show_section_footer():
    """
    Displays the footer section with a motivational message.
    """
    st.markdown("<h2 style='text-align: center;'>Use the power of LLMs to boost your job search 💻</h2>", unsafe_allow_html=True)
