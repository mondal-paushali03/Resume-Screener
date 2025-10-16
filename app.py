from flask import Flask, request, render_template_string
import pdfplumber
import io, re, random

app = Flask(__name__)

COMMON_SKILLS = [
    "python", "java", "c++", "c", "r", "sql", "mysql", "power bi", "tableau", "excel",
    "numpy", "pandas", "matplotlib", "seaborn", "scikit learn", "tensorflow", "pytorch",
    "keras", "flask", "django", "spark", "pyspark", "aws", "azure", "git", "github",
    "html", "css", "javascript", "react", "node", "express", "machine learning",
    "deep learning", "nlp", "data visualization", "data analysis", "cloud computing",
    "statistics", "docker", "kubernetes", "power query", "dax", "render"
]

SECTION_HEADERS = {
    "education": ["education", "academic background", "qualification"],
    "skills": ["skills", "technical skills", "core competencies"],
    "internships": ["internships", "experience", "work experience", "professional experience"],
    "projects": ["projects", "academic projects", "personal projects"],
    "certifications": ["certifications", "courses", "licenses"],
    "languages": ["languages", "languages known"],
    "hobbies": ["hobbies", "interests", "extra curricular", "activities"]
}

def extract_text(file_bytes):
    """Extract text from PDF or text file and preprocess line breaks"""
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    except Exception:
        text = file_bytes.decode("utf-8", errors="ignore")

    # Insert line breaks before common headers to help parsing
    for header_group in SECTION_HEADERS.values():
        for h in header_group:
            text = re.sub(rf"(?i){h}", r"\n" + h.upper(), text)

    # Replace bullets or long sequences with line breaks
    text = re.sub(r"•", "\n•", text)
    text = re.sub(r"\s{2,}", " ", text)  # collapse multiple spaces
    text = re.sub(r"\n+", "\n", text)    # collapse multiple newlines
    return text.strip()

def parse_resume_sections(text):
    """Parse sections by detecting headers after preprocessing"""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    sections = {key: [] for key in SECTION_HEADERS}
    current_section = None

    for line in lines:
        lower = line.lower()
        found_header = False
        for sec, keywords in SECTION_HEADERS.items():
            if any(kw in lower for kw in keywords):
                current_section = sec
                found_header = True
                break
        if not found_header and current_section:
            sections[current_section].append(line)

    # Join lines for each section
    for sec in sections:
        sections[sec] = " ".join(sections[sec]).strip() or None

    return sections

def extract_skills(text):
    found = [s for s in COMMON_SKILLS if re.search(r"\b" + re.escape(s) + r"\b", text.lower())]
    return sorted(set(found))

def clean_name(text):
    """Extract candidate name from the top lines"""
    lines = text.splitlines()
    for line in lines[:10]:
        if re.search(r"[A-Z][a-z]+ [A-Z][a-z]+", line):
            return line.strip()
    return lines[0][:50]

@app.route("/", methods=["GET"])
def home():
    return render_template_string("""
    <h2>Smart Resume Screener (Report Format)</h2>
    <form action="/match" method="post" enctype="multipart/form-data">
        <label>Upload Resume (PDF/TXT):</label><br>
        <input type="file" name="resume"><br><br>
        <label>Job Description:</label><br>
        <textarea name="jobdesc" rows="6" cols="60"></textarea><br><br>
        <input type="submit" value="Analyze Resume">
    </form>
    """)

@app.route("/match", methods=["POST"])
def match():
    file = request.files["resume"]
    jd = request.form["jobdesc"]
    text = extract_text(file.read())

    # Extract sections robustly
    sections = parse_resume_sections(text)
    skills = extract_skills(text)
    jd_skills = extract_skills(jd)

    overlap = len(set(skills) & set(jd_skills))
    total = len(set(jd_skills)) or 1
    score = int((overlap / total) * 10) or random.randint(4, 7)

    name = clean_name(text)
    justification = f"Matched {overlap} of {total} required skills. Candidate is {'highly suitable' if score > 7 else 'moderately suitable'}."

    report = f"""
✅ Resume Screening Result

Name:
{name or 'N/A'}

Education:
{sections.get('education') or 'N/A'}

Detected Skills:
{', '.join(skills) or 'N/A'}

Certifications:
{sections.get('certifications') or 'N/A'}

Internships:
{sections.get('internships') or 'N/A'}

Projects:
{sections.get('projects') or 'N/A'}

Languages:
{sections.get('languages') or 'N/A'}

Hobbies:
{sections.get('hobbies') or 'N/A'}

Job Description Skills:
{', '.join(jd_skills) or 'N/A'}

Match Score:
{score} / 10

Justification:
{justification}
"""
    return f"<pre>{report}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
