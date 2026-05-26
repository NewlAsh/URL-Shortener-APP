# 🔗 URL Shortener App

> A modern full-stack URL shortener application built with FastAPI, SQLAlchemy, and a clean minimal frontend.
>
> This project allows users to generate compact short links, redirect instantly to original URLs, and interact with a polished frontend interface connected to a fully custom Python backend.
>
> Developed as a backend-focused learning project with emphasis on API design, database handling, clean architecture, and frontend integration.

---

# ✨ Features

* Convert long URLs into compact short links
* Fast redirection using generated short codes
* Clean and responsive frontend interface
* Custom short code generation
* Database persistence using SQLAlchemy ORM
* Proper REST API structure
* HTTP exception handling with meaningful responses
* Minimal modern UI with smooth interactions
* Full frontend-backend integration
* Organized project structure for scalability

---

# 🛠 Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Backend    | FastAPI               |
| ORM        | SQLAlchemy            |
| Database   | SQLite                |
| Validation | Pydantic              |
| Frontend   | HTML, CSS, JavaScript |
|            |                       |

---

# ⚙️ How The Application Works

### 1. User submits a URL

The frontend sends a request to the FastAPI backend containing the original long URL.

### 2. Backend processes the request

The backend:

* validates the URL
* generates a short unique code
* stores the mapping inside the database
* returns the shortened URL response

### 3. User visits the shortened link

When the short link is opened:

* the backend searches the database
* finds the original URL
* redirects the user instantly

---

# 🧱 Project Structure

```bash
url-shortener/
│
├── main_url.py              # FastAPI application entry point
├── main_model.py            # SQLAlchemy models
├── main_database.py         # Database configuration
├── main_schemas.py          # Pydantic schemas
├── main_utils.py            # Utility functions / short code generator
├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/url-shortener.git

cd url-shortener
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the FastAPI server

```bash
uvicorn main_url:app --reload
```

You should now see:

```bash
Uvicorn running on http://127.0.0.1:8000
```

---

## 5. Open the frontend

Open the frontend files in your browser and interact with the application.

The frontend communicates directly with your FastAPI backend.

---

# 📌 API Endpoints

| Method | Endpoint        | Description              |
| ------ | --------------- | ------------------------ |
| POST   | `/shorten`      | Create a shortened URL   |
| GET    | `/{short_code}` | Redirect to original URL |

---

# 📄 Example Request

## Create Short URL

```json
POST /shorten

{
  "url": "https://www.example.com"
}
```

---

# 📄 Example Response

```json
{
  "short_url": "http://127.0.0.1:8000/abc123"
}
```

---

# 🧠 What I Learned

### FastAPI Fundamentals

* Building REST APIs
* Route handling
* Request/response management
* HTTP status codes

### SQLAlchemy ORM

* Database models
* Sessions and transactions
* ORM-based database operations

### Pydantic Validation

* Request validation
* Response schemas
* Data serialization

### Backend Architecture

* Separating logic into modules
* Keeping code maintainable
* Organizing scalable backend structure

### Frontend Integration

* Connecting frontend with APIs
* Fetch requests and async handling
* Managing frontend responses cleanly

---

# 🎨 Frontend Design Goals

The frontend was intentionally designed to be:

* clean
* minimal
* modern
* responsive
* visually polished

The goal was to create something that feels like a real full-stack application without relying on flashy neon effects or overly complicated UI design.

---

# ⚠️ Disclaimer

The backend logic for this project was fully written and structured by me using FastAPI and SQLAlchemy.

The frontend styling and layout were created with AI-assisted design iteration based on detailed requirements and frontend direction provided by me.

---

# 👨‍💻 Author

Built by Kalash Desai.

Feel free to fork the project, explore the codebase, and improve upon it.
