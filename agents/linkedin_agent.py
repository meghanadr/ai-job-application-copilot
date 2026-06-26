from utils.llm import llm


def generate_linkedin_message(resume_text, jd_text):
    """
    Generate a professional LinkedIn connection request
    or referral message based on the candidate's resume
    and the job description.
    """

    prompt = f"""
    You are an expert LinkedIn career coach.

    Candidate Resume:
    ------------------------
    {resume_text}

    Job Description:
    ------------------------
    {jd_text}

    Generate THREE different LinkedIn messages.

    -----------------------------
    Message 1: Recruiter
    -----------------------------
    Write a short LinkedIn message (80-120 words)
    expressing interest in the role.

    -----------------------------
    Message 2: Employee Referral
    -----------------------------
    Write a polite message requesting a referral.

    -----------------------------
    Message 3: Hiring Manager
    -----------------------------
    Write a professional message introducing yourself,
    highlighting relevant experience, and expressing
    interest in the position.

    Guidelines:

    • Keep the tone professional and friendly.
    • Do not exaggerate experience.
    • Mention matching skills from the resume.
    • Mention enthusiasm for the opportunity.
    • End with a polite thank you.

    Format each message separately using headings.
    """

    response = llm.invoke(prompt)

    return response.content