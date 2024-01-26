import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(file):
    reader = pdf.PdfReader(file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text)
    return text



# Streamlit

st.title("CraftCover")
st.text("Create the perfect cover letter!")
job_title = st.text_area("Insert Job Title")
job_description = st.text_area("Insert Job Description")
file = st.file_uploader("Upload Your Resume", type="pdf", help="Upload only PDF files")
input_prompt = f"""
You are an extremely qualified resume/curriculum vitae reviewer, with a deep understanding of what recruiters look for in a cover letter. Your task is to evaluate the information provided in the given resume and craft a perfect, persuasive and convincing cover letter that's suitable for the job title of {job_title}. Make sure the cover letter emphasizes the person's ability to contribute to the organization and their skills, pertaining to the job description as provided : {job_description}. Here's the resume: {file}
"""
submit = st.button("Submit")

if submit:
    if file is not None:
        resume = input_pdf_text(file)
        response = get_response(input_prompt)
        st.subheader(response)