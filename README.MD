# Smart Resume Screener

**Intelligently parse resumes, extract skills, and match candidates with a given job description using Python and Flask.**

---

## Features

- Upload PDF or text resumes through a web interface.
- Extract structured sections from resumes:
  - Name
  - Education
  - Technical Skills
  - Certifications
  - Internships / Work Experience
  - Projects
  - Languages
  - Hobbies / Extra-curricular
- Detect skills automatically from resume content and job description.
- Compute a **match score (1–10)** based on skill overlap.
- Generate a **human-readable report** with:
  - Detected skills
  - Job description skills
  - Match score
  - Justification
- Works even with messy resumes extracted from PDFs.

---

## Installation & Setup

Copy and paste the following commands into your terminal to set up and run the project:

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/smart-resume-screener.git
cd smart-resume-screener

# 2. Create a Python virtual environment
python -m venv venv

# 3. Activate the virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install required Python packages
pip install -r requirements.txt

# If requirements.txt does not exist, generate it after installing manually
# pip install Flask pdfplumber
# pip freeze > requirements.txt

# 5. Run the Flask app
python app.py

# 6. Open your browser and go to:
# http://127.0.0.1:5000

# 7. Upload a resume (PDF/TXT) and enter the job description.
# 8. Click "Analyze Resume" to see the human-readable screening report.
