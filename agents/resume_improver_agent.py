from utils.llm import llm


def improve_resume(resume_text: str, jd_text: str) -> str:
    """
    Improve a resume based on the given Job Description.
    """

    prompt = f"""
You are an expert ATS Resume Reviewer and Technical Recruiter.

Compare the candidate's resume with the Job Description.

Candidate Resume:
-----------------
{resume_text}

Job Description:
-----------------
{jd_text}

Provide the following:

1. ATS Score (out of 100)

2. Resume Strengths

3. Resume Weaknesses

4. Missing Keywords

5. Missing Technical Skills

6. Improved Professional Summary

7. Improved Project Descriptions

8. Better Resume Bullet Points

9. ATS Optimization Suggestions

10. Final Recommendations

Format the response nicely using headings and bullet points.
"""

    response = llm.invoke(prompt)

    return response.content