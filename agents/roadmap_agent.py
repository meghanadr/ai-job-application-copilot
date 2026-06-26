from utils.llm import llm


def generate_learning_roadmap(resume_text, jd_text):
    """
    Generate a personalized learning roadmap
    based on the resume and job description.
    """

    prompt = f"""
    You are an Expert AI Career Coach and Senior Software Engineer.

    Candidate Resume:
    ----------------------------------
    {resume_text}

    Job Description:
    ----------------------------------
    {jd_text}

    Analyze both documents and create a personalized learning roadmap.

    Include the following sections:

    ## 1. Current Skill Level
    - Beginner
    - Intermediate
    - Advanced

    Explain why.

    ## 2. Missing Skills
    List all missing skills required for this job.

    ## 3. Priority Learning Order
    Arrange the skills from highest priority to lowest priority.

    ## 4. 30-Day Learning Plan

    Week 1
    - Topics
    - Practice Tasks
    - Mini Project

    Week 2
    - Topics
    - Practice Tasks
    - Mini Project

    Week 3
    - Topics
    - Practice Tasks
    - Mini Project

    Week 4
    - Topics
    - Practice Tasks
    - Mini Project

    ## 5. Recommended Resources

    Suggest:
    - Documentation
    - YouTube Channels
    - GitHub Projects
    - Free Courses
    - Practice Websites

    ## 6. Portfolio Projects

    Suggest 5 real-world projects that match this job.

    ## 7. Interview Preparation Plan

    Explain what to revise before interviews.

    ## 8. Daily Study Schedule

    Create a daily 2-hour study plan.

    ## 9. Expected Outcome

    Explain what the candidate should achieve after completing the roadmap.

    Format everything using headings, tables, and bullet points.
    """

    response = llm.invoke(prompt)

    return response.content