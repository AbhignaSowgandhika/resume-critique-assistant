import streamlit as st
from utils.parser import extract_text_from_pdf, extract_sections
from utils.llm_eval import generate_feedback

st.title("📄 Resume Critique Assistant")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description")

if resume_file and jd_text:
    with open("data/temp_resume.pdf", "wb") as f:
        f.write(resume_file.read())
    
    raw_text = extract_text_from_pdf("data/temp_resume.pdf")
    sections = extract_sections(raw_text)

    with st.spinner("Analyzing..."):
        feedback = generate_feedback(sections, jd_text)

    st.subheader("💬 Feedback")
    st.write(feedback)
