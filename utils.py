
# utils.py
# Utility functions for extracting text from PDF and uploaded files in the CV Analyzer app.

import PyPDF2
import io


def extract_text_from_pdf(pdf_file):
    """
    Extracts all text from a PDF file.
    Args:
        pdf_file: A file-like object containing the PDF.
    Returns:
        str: The extracted text from all pages.
    """
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_text_from_file(uploaded_file):
    """
    Extracts text from an uploaded file (PDF or TXT).
    Args:
        uploaded_file: The uploaded file from Streamlit uploader.
    Returns:
        str: The extracted text.
    """
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")


