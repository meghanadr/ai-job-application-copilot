from utils.llm import llm


def generate_email(resume_text, jd_text):
    """
    Generate a professional job application email
    based on the candidate's resume and job description.
    """

    prompt = f"""
    You are an expert recruiter and career coach.

    Write a professional job application email using the
    candidate's resume and the job description.

    Candidate Resume:
    ------------------------
    {resume_text}

    Job Description:
    ------------------------
    {jd_text}

    Instructions:

    - Write a professional email.
    - Mention interest in the position.
    - Highlight relevant skills and experience.
    - Mention that the resume is attached.
    - Keep the email between 150 and 200 words.
    - End with a polite thank-you and professional closing.

    Return the email in the following format:

    Subject:
    ...

    Email:
    ...
    """

    response = llm.invoke(prompt)

    return response.content