import spacy
from PyPDF2 import PdfReader

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    return " ".join([page.extract_text() for page in reader.pages])

def extract_sections(text):
    doc = nlp(text)
    lines = text.split('\n')
    sections = {"skills": "", "experience": "", "education": ""}

    for line in lines:
        lower = line.lower()
        if "skill" in lower:
            sections["skills"] += line + "\n"
        elif "experience" in lower or "worked" in lower:
            sections["experience"] += line + "\n"
        elif "education" in lower:
            sections["education"] += line + "\n"
    return sections
