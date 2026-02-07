# Profile Playground

A minimal full-stack playground that stores my personal profile data in a SQL database and exposes it via a FastAPI backend with queryable APIs and a lightweight frontend.

This project was built as part of a backend assessment.

---

## 🏗️ Architecture

Frontend (HTML/CSS/JS)
|
| fetch() (CORS enabled)
v
FastAPI Backend
|
v
SQLite Database



- **Backend**: FastAPI + SQLAlchemy
- **Database**: SQLite (local), easily portable to PostgreSQL
- **Frontend**: Minimal vanilla HTML/CSS/JS
- **API Style**: REST

---

## 📁 Project Structure

profile-playground/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── database.py
│ │ ├── models.py
│ │ ├── schemas.py
│ │ └── routers/
│ │ ├── health.py
│ │ ├── profile.py
│ │ ├── projects.py
│ │ ├── skills.py
│ │ └── search.py
│ │
│ ├── app.db # SQLite database (generated)
│ ├── apply_seed.py # Applies seed.sql to DB
│ └── verify_db.py # Verifies DB contents
│
├── database/
│ ├── schema.sql # DB schema
│ └── seed.sql # Initial seed data (my real profile)
│
├── frontend/
│ ├── index.html
│ ├── styles.css
│ └── app.js
│
├── README.md
└── .gitignore


---

## 🗄️ Database Schema

### Tables
- **profile**
  - name, email, education
  - github, linkedin, portfolio

- **skills**
  - name, count

- **projects**
  - title, description, link

- **project_skills**
  - project_id, skill_id (many-to-many mapping)

Schema is defined in `database/schema.sql`.

---

## 🌱 Seed Data

Initial data (my real profile, skills, and projects) is stored in:

Seed data is **not auto-applied**.  
It must be explicitly executed using:

```bash
python apply_seed
```

#🚀 Backend Setup (Local)
1️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies
pip install fastapi uvicorn sqlalchemy python-dotenv

3️⃣ Apply schema & seed
python apply_seed.py

4️⃣ Run backend
uvicorn app.main:app


Backend runs at:

http://127.0.0.1:8000


Swagger docs:

http://127.0.0.1:8000/docs

🔌 API Endpoints
Health Check
GET /health

Profile
GET    /profile
POST   /profile
PUT    /profile

Projects by Skill
GET /projects?skill=python


Top Skills
GET /skills/top


Search Projects
GET /search?q=movie


🧪 Sample cURL Commands
```curl http://127.0.0.1:8000/health```

```curl http://127.0.0.1:8000/profile```

```curl "http://127.0.0.1:8000/projects?skill=python"```

```curl http://127.0.0.1:8000/skills/top```

```curl "http://127.0.0.1:8000/search?q=api"```

🎨 Frontend

Minimal single-page UI

Built using vanilla HTML, CSS, and JavaScript

Fetches data from the hosted backend APIs

Supports:

Profile display

Project listing

Search by skill

To run frontend:

Open frontend/index.html in browser

⚠️ Known Limitations

No authentication (single-user system)

No pagination

SQLite used for simplicity (PostgreSQL recommended for production)

Minimal UI by design

🔮 Future Improvements

PostgreSQL migration

Authentication

Pagination & filtering

Docker support

CI/CD pipeline

👤 Author

Vinayak Khandelwal

GitHub: https://github.com/vinayakkhandelwal

LinkedIn: https://linkedin.com/in/vinayakkhandelwal


