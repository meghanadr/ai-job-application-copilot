from utils.llm import llm


def generate_cover_letter(resume_text, jd_text):
    """
    Generate a professional cover letter
    based on the resume and job description.
    """

    prompt = f"""
    You are an expert career coach and professional recruiter.

    Write a personalized cover letter using the candidate's resume
    and the job description.

    Candidate Resume:
    -----------------------
    {resume_text}

    Job Description:
    -----------------------
    {jd_text}

    Instructions:

    - Keep the cover letter between 300 and 400 words.
    - Use a professional and confident tone.
    - Explain why the candidate is a strong fit.
    - Highlight the candidate's most relevant skills and projects.
    - Mention how the candidate's experience aligns with the job requirements.
    - End with a strong closing paragraph expressing enthusiasm.

    Return only the cover letter.
    """

    response = llm.invoke(prompt)

    return response.content