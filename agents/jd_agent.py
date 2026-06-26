from utils.llm import llm


def analyze_job_description(jd_text):
    """
    Analyze the Job Description and extract hiring requirements.
    """

    prompt = f"""
    You are an expert Job Description Analyzer.

    Analyze the following Job Description.

    Extract:

    1. Job Title
    2. Required Skills
    3. Preferred Skills
    4. Programming Languages
    5. Frameworks
    6. Databases
    7. Cloud Technologies
    8. Tools
    9. Years of Experience
    10. Responsibilities

    Format the response using headings and bullet points.

    Job Description:

    {jd_text}
    """

    response = llm.invoke(prompt)

    return response.content