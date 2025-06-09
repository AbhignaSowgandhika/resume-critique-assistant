from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

def generate_feedback(sections, jd_text):
    with open("prompts/critique_template.txt", "r", encoding="utf-8") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["skills", "experience", "education", "job_description"],
        template=template
    )

    llm = Ollama(model="mistral")
    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run({
        "skills": sections.get("skills", ""),
        "experience": sections.get("experience", ""),
        "education": sections.get("education", ""),
        "job_description": jd_text
    })
