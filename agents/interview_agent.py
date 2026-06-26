from utils.llm import llm


def generate_interview_questions(resume_text, jd_text):
    """
    Generate personalized interview questions and answers
    based on the candidate's resume and job description.
    """

    prompt = f"""
    You are a Senior Technical Interviewer.

    Candidate Resume:
    ---------------------
    {resume_text}

    Job Description:
    ---------------------
    {jd_text}

    Generate a complete interview preparation guide.

    Include the following sections:

    ## 1. HR Interview Questions
    - Generate 5 HR interview questions.
    - Provide detailed sample answers.

    ## 2. Technical Interview Questions
    - Generate 10 technical questions based on the candidate's skills.
    - Provide detailed answers.

    ## 3. Scenario-Based Questions
    - Generate 5 real-world scenario questions.
    - Provide ideal answers.

    ## 4. Coding Interview Questions
    - Suggest 5 coding problems relevant to the job.
    - Mention the difficulty level (Easy, Medium, Hard).

    ## 5. Project-Based Questions
    - Ask questions about the candidate's projects.
    - Provide guidance on how to answer them.

    ## 6. Tips
    - Common interview mistakes.
    - Interview preparation tips.
    - Final-day checklist.

    Format the response using proper headings and bullet points.
    """

    response = llm.invoke(prompt)

    return response.content