from utils.llm import llm


def analyze_match(resume_text, jd_text):
    """
    Compare the Resume with the Job Description
    and generate a detailed match analysis.
    """

    prompt = f"""
    You are an expert ATS Resume Evaluator and Hiring Manager.

    Compare the candidate's Resume with the Job Description.

    Resume:
    -----------------------
    {resume_text}

    Job Description:
    -----------------------
    {jd_text}

    Provide a professional report with the following sections.

    ## 1. Overall Match Score
    Give an ATS Match Score out of 100%.

    ## 2. Matching Skills
    List all skills that match between the resume and the job description.

    ## 3. Missing Skills
    List the important skills that are missing from the resume.

    ## 4. Strengths
    Mention the strongest points of the candidate.

    ## 5. Weaknesses
    Mention the weaknesses or missing experience.

    ## 6. ATS Keyword Analysis
    Mention important keywords missing from the resume.

    ## 7. Suggestions to Improve
    Suggest how the candidate can improve the resume to increase the match score.

    Format the response using proper headings, bullet points and tables wherever suitable.
    """

    response = llm.invoke(prompt)

    return response.content