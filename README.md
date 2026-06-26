# 🤖 AI Job Application Copilot

An AI-powered application that helps job seekers analyze resumes, compare them with job descriptions, identify skill gaps, improve resumes, generate personalized learning roadmaps, prepare interview questions, and create professional application content.

---

## 🚀 Features

### 📄 Resume Analysis
- Extract technical skills
- Programming languages
- Frameworks
- Databases
- Tools
- Certifications

### 📋 Job Description Analysis
- Required skills
- Preferred skills
- Technologies
- Tools
- Experience requirements

### 🎯 Resume vs Job Match
- ATS Match Score
- Matching skills
- Missing skills
- Skill gap analysis
- Suggestions for improvement

### 📄 Resume Improvement
- ATS optimization
- Missing keywords
- Resume summary improvement
- Better project descriptions
- Improved bullet points

### 📚 Learning Roadmap
- 30-Day personalized roadmap
- Weekly learning plan
- Recommended resources
- Mini projects

### 🎤 Interview Preparation
- Beginner questions
- Intermediate questions
- Advanced questions
- Sample answers

### ✉️ Cover Letter Generator

Generate personalized cover letters tailored to the job description.

### 📧 Job Application Email

Generate professional recruiter emails.

### 💼 LinkedIn Outreach Message

Generate personalized LinkedIn messages for recruiters.

---

# 🛠 Tech Stack

- Python
- Streamlit
- OpenAI GPT-4o Mini
- LangChain
- PyPDF
- python-dotenv

---

# 📂 Project Structure

```
ai-job-application-copilot/

│
├── agents/
│   ├── resume_agent.py
│   ├── jd_agent.py
│   ├── match_agent.py
│   ├── roadmap_agent.py
│   ├── interview_agent.py
│   ├── resume_improver_agent.py
│   ├── cover_letter_agent.py
│   ├── email_agent.py
│   └── linkedin_agent.py
│
├── utils/
│   ├── llm.py
│   └── pdf_reader.py
│
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/meghanadr/ai-job-application-copilot.git
```

Move into the project

```bash
cd ai-job-application-copilot
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
OPENAI_API_KEY=your_api_key_here
```

Run

```bash
streamlit run app.py
```

---

# 📸 Screenshots

## Home Page

(Add Screenshot Here)

## Resume Analysis

(Add Screenshot Here)

## Match Analysis

(Add Screenshot Here)

## Learning Roadmap

(Add Screenshot Here)

## Interview Questions

(Add Screenshot Here)

---

# 🚀 Future Roadmap

- LangGraph Multi-Agent Workflow
- Supervisor Agent
- Memory
- Vector Database
- RAG Pipeline
- Resume Chat
- AI Career Coach
- Company Research Agent
- Salary Prediction
- Resume Version Management

---

# 👩‍💻 Author

**Meghana DR**

GitHub:
https://github.com/meghanadr

LinkedIn:
https://www.linkedin.com/in/meghana-d-r/

---

⭐ If you found this project useful, consider giving it a Star!
