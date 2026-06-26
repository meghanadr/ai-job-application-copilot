from utils.llm import llm


def analyze_resume(resume_text):

    prompt = f"""
    You are an expert Resume Analyzer.

    Analyze the resume and extract:

    1. Technical Skills
    2. Programming Languages
    3. Frameworks
    4. Databases
    5. Tools
    6. Certifications

    Resume:

    {resume_text}
    """

    response = llm.invoke(prompt)

    return response.content