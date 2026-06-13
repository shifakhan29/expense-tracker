# 💸 Expense Tracker API

A REST API built while learning backend development. 
Covers full CRUD, database integration, and JWT authentication.

> Built by a CS student actively learning industry-level backend development.

## 🛠️ Tech Stack
- **Python + Flask** — REST API
- **SQLAlchemy + SQLite** — Database & ORM
- **JWT + bcrypt** — Authentication & Password Hashing

## 🔗 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/register` | Register new user | ❌ |
| POST | `/login` | Login & get JWT token | ❌ |
| GET | `/expenses` | Get all expenses | ✅ |
| POST | `/expenses` | Add new expense | ✅ |
| PUT | `/expenses/<id>` | Update expense | ✅ |
| DELETE | `/expenses/<id>` | Delete expense | ✅ |

## ⚙️ Setup & Run
```bash
git clone https://github.com/shifakhan29/expense-tracker.git
cd expense-tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## 📌 Status
> 🚧 In progress — Authentication done, deployment coming soon.

## 👩‍💻 Author
**Shifa Khan** — CS Student  
[GitHub](https://github.com/shifakhan29)
