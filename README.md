# Mentor Blog 

A simple Django blog project created as part of my backend developer learning path.

---

##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/payloadhacker/mentor_blog.git
cd mentor_blog

2. Create a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run initial migrations
python manage.py migrate

5. Run the development server
python manage.py runserver


Visit: http://127.0.0.1:8000

## Project Structure
mentor_blog/
│
├── mentor_blog/         # Project configuration (settings, urls, wsgi)
├── posts/               # Blog app
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
│
├── manage.py
├── requirements.txt
└── README.md

## Branches

feature/init-project — initial Django setup

 ### Tech Stack

Python 3.10+

Django 5.x

SQLite (default for development)

Git + GitHub for version control

 ## Notes

This project is part of my structured Django backend learning journey.

Mentor: ChatGPT (AI coding mentor)