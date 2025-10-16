# 🚀 Smart Resume Screener

**Intelligently parse resumes, extract skills, and match candidates with a job description using Python and Flask.**

---

## 🌟 Features

- 📄 Upload **PDF or text resumes** through a simple web interface.
- 🏫 Extract structured sections from resumes:
  - Name
  - Education
  - Technical Skills
  - Certifications
  - Internships / Work Experience
  - Projects
  - Languages
  - Hobbies / Extra-curricular
- 🔍 Detect **skills automatically** from resume content and job description.
- 🎯 Compute a **match score (1–10)** based on skill overlap.
- 📝 Generate a **human-readable report** including:
  - Detected skills
  - Job description skills
  - Match score
  - Justification
- 💡 Works even with messy resumes extracted from PDFs.
- ⚡ Lightweight — no database required, runs locally.

---

## 🛠 Installation & Setup

Follow these steps to get started:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/smart-resume-screener.git
cd smart-resume-screener

# 2️⃣ Create a Python virtual environment
python -m venv venv

# 3️⃣ Activate the virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4️⃣ Install required packages
pip install -r requirements.txt

# ⚠️ If requirements.txt is missing, install manually and generate it
# pip install Flask pdfplumber
# pip freeze > requirements.txt
