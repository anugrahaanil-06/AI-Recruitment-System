# AI-Recruitment-System

An **AI-powered recruitment platform** built using **Django and Python** that helps recruiters automatically evaluate candidate resumes based on job skill requirements.



## Features

* Post job openings
* Candidates can apply for jobs
* Upload resumes (PDF)
* Automatic resume text extraction
* Skill matching with job requirements
* Match score calculation between resume and job skills
* Admin panel for job management



## Technologies Used

* Python
* Django
* SQLite
* HTML
* PyPDF2 (for resume parsing)



## How It Works

1. Admin adds a job with required skills.
2. Candidate applies and uploads their resume.
3. System extracts text from the resume.
4. Skills in the resume are compared with job requirements.
5. A **match score** is generated automatically.



# Installation

```bash
git clone https://github.com/anugrahaanil-06/AI-Recruitment-System.git
cd AI-Recruitment-System
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```



## Future Improvements

* NLP based semantic skill matching
* Resume ranking system
* Recruiter dashboard
* Job recommendation system
* AI-based resume screening



# Author

**Anugraha AL**

