import streamlit as st

from utils.pdf_reader import extract_text
from agents.resume_agent import analyze_resume
print("resume_agent OK")

from agents.jd_agent import analyze_job_description
print("jd_agent OK")

from agents.match_agent import analyze_match
print("match_agent OK")

from agents.roadmap_agent import generate_learning_roadmap
print("roadmap_agent OK")

from agents.interview_agent import generate_interview_questions
print("interview_agent OK")

from agents.resume_improver_agent import improve_resume
print("resume_improver_agent OK")

from agents.cover_letter_agent import generate_cover_letter
print("cover_letter_agent OK")

from agents.linkedin_agent import generate_linkedin_message
print("linkedin_agent OK")

from agents.email_agent import generate_email
print("email_agent OK")

# ---------------------------------------------------
# Streamlit Config
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Job Application Copilot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("🤖 AI Job Application Copilot")

st.markdown("""
Welcome!

Upload your Resume and Job Description.

The AI Copilot can:

- 📑 Analyze Resume
- 📋 Analyze Job Description
- 🎯 Calculate ATS Match Score
- 📄 Improve Resume
- 📚 Generate Learning Roadmap
- 🎤 Generate Interview Questions
- ✉️ Generate Cover Letter
- 📧 Generate Job Application Email
- 💼 Generate LinkedIn Messages
""")

# ---------------------------------------------------
# Upload Section
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"]
    )

with col2:
    jd_file = st.file_uploader(
        "📋 Upload Job Description",
        type=["pdf"]
    )

# ---------------------------------------------------
# Analyze Button
# ---------------------------------------------------

if st.button("🚀 Analyze Profile"):

    if resume_file is None or jd_file is None:
        st.error("Please upload both Resume and Job Description.")
        st.stop()

    # ---------------------------------------------------
    # Extract PDF Text
    # ---------------------------------------------------

    with st.spinner("Reading PDFs..."):
        resume_text = extract_text(resume_file)
        jd_text = extract_text(jd_file)

    # ---------------------------------------------------
    # Resume Agent
    # ---------------------------------------------------

    with st.spinner("Analyzing Resume..."):
        resume_result = analyze_resume(resume_text)

    # ---------------------------------------------------
    # JD Agent
    # ---------------------------------------------------

    with st.spinner("Analyzing Job Description..."):
        jd_result = analyze_job_description(jd_text)

    # ---------------------------------------------------
    # Match Agent
    # ---------------------------------------------------

    with st.spinner("Calculating Match Score..."):
        match_result = analyze_match(
            resume_text,
            jd_text
        )

    # ---------------------------------------------------
    # Resume Improver Agent
    # ---------------------------------------------------

    with st.spinner("Improving Resume..."):
        improve_result = improve_resume(
            resume_text,
            jd_text
        )

    # ---------------------------------------------------
    # Roadmap Agent
    # ---------------------------------------------------

    with st.spinner("Generating Learning Roadmap..."):
        roadmap_result = generate_learning_roadmap(
            resume_text,
            jd_text
        )

    # ---------------------------------------------------
    # Interview Agent
    # ---------------------------------------------------

    with st.spinner("Generating Interview Questions..."):
        interview_result = generate_interview_questions(
            resume_text,
            jd_text
        )

    # ---------------------------------------------------
    # Cover Letter Agent
    # ---------------------------------------------------

    with st.spinner("Generating Cover Letter..."):
        cover_letter_result = generate_cover_letter(
            resume_text,
            jd_text
        )

    # ---------------------------------------------------
    # Email Agent
    # ---------------------------------------------------

    with st.spinner("Generating Job Email..."):
        email_result = generate_email(
            resume_text,
            jd_text
        )

    # ---------------------------------------------------
    # LinkedIn Agent
    # ---------------------------------------------------

    with st.spinner("Generating LinkedIn Messages..."):
        linkedin_result = generate_linkedin_message(
            resume_text,
            jd_text
        )

    st.success("✅ Analysis Complete!")

    # ---------------------------------------------------
    # Tabs
    # ---------------------------------------------------

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(
        [
            "📑 Resume",
            "📋 Job Description",
            "🎯 Match",
            "📄 Resume Improvement",
            "📚 Roadmap",
            "🎤 Interview",
            "✉️ Cover Letter",
            "📧 Email",
            "💼 LinkedIn"
        ]
    )

    with tab1:
        st.header("Resume Analysis")
        st.write(resume_result)

    with tab2:
        st.header("Job Description Analysis")
        st.write(jd_result)

    with tab3:
        st.header("Resume vs Job Match")
        st.write(match_result)

    with tab4:
        st.header("Resume Improvement Suggestions")
        st.write(improve_result)

    with tab5:
        st.header("Learning Roadmap")
        st.write(roadmap_result)

    with tab6:
        st.header("Interview Preparation")
        st.write(interview_result)

    with tab7:
        st.header("Cover Letter")
        st.write(cover_letter_result)

    with tab8:
        st.header("Job Application Email")
        st.write(email_result)

    with tab9:
        st.header("LinkedIn Messages")
        st.write(linkedin_result)