# Job & Skill Match Tracker

A Django and Django REST Framework (DRF) application for tracking job applications and comparing resume skills against job descriptions to surface match percentages and missing technical keywords.

## Features
- **Application Tracking:** Log and manage job applications with company, role, status (`Applied`, `Interview`, `Offer`, `Rejected`), job description, and application date.
- **Keyword & Skill Gap Analysis:** Evaluates job descriptions against a user's saved skills to calculate a match score and highlight missing keywords.
- **Status Filtering & Updates:** Filter applications by status, update progress, and remove records.
- **REST API (`DRF`):** Exposes JSON endpoints under `/api/applications/` for programmatic access or a separate frontend (such as React or Next.js).

## Tech Stack
- **Backend:** Python, Django, Django REST Framework
- **Database:** SQLite (default local development) / PostgreSQL
- **Frontend:** Django Templates + Tailwind CSS (replaceable with Next.js / React)

## Project Structure
```text
skillmatch/
├── config/          # Project settings, root URLs, WSGI/ASGI entry points
├── tracker/         # Models, keyword matcher, views, serializers, forms, templates
├── manage.py
└── README.md
```

## Local Setup

1. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux / macOS:
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

3. **Apply migrations and create an admin user**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

Open `http://127.0.0.1:8000/` in your browser.

