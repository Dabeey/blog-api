# Blog API

A RESTful blog backend API built with Python / FastAPI (or framework you used).  
Supports user authentication, posts, comments, and categories.

---

## Features

- User registration, login, authentication (e.g. JWT)  
- CRUD operations for blog posts  
- CRUD operations for comments  
- CRUD for categories / tags  
- Relationship mapping (post ↔ author, comments ↔ posts)  
- Input validation via Pydantic  
- Auto-generated API docs (Swagger / Redoc)  
- Error handling and status codes  

---

## Tech Stack

- **Python 3.x**  
- **FastAPI** (or your chosen web framework)  
- **SQLAlchemy / ORM**  
- **Pydantic**  
- **Uvicorn** (ASGI server)  
- **Database**: SQLite / PostgreSQL / MySQL (configurable)  
- (Optional) **Alembic** for migrations  

---

## Installation & Setup

1. Clone repository  
   ```bash
   git clone https://github.com/Dabeey/blog-api.git
   cd blog-api

Create and activate virtual environment

python -m venv venv
source venv/bin/activate     # Linux / macOS  
venv\Scripts\activate        # Windows  


Install dependencies

pip install -r requirements.txt


Configure environment variables
Create a .env file (or use settings) with keys like:

DATABASE_URL=…
SECRET_KEY=…
DEBUG=True


(If you use migrations) Run migrations

alembic upgrade head


Run server

uvicorn app.main:app --reload

Endpoints & Usage

Open your browser on:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Typical endpoints (adjust your route prefixes accordingly):

Method	Path	Description
POST	/auth/register	Register a new user
POST	/auth/login	Authenticate and get token
GET	/posts	List all blog posts
POST	/posts	Create new post
GET	/posts/{id}	Get a single post
PUT	/posts/{id}	Update a post
DELETE	/posts/{id}	Delete a post
GET	/posts/{id}/comments	List comments for a post
POST	/posts/{id}/comments	Add a comment to a post
CRUD for categories/tags similarly		

Include Authorization header Bearer <token> on protected routes.

Project Structure (example)
blog-api/
│
├── app/
│   ├── main.py           # Entry point
│   ├── models.py         # ORM models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # DB access logic
│   ├── routers/           # API route modules
│   ├── dependencies.py    # Dependencies, auth logic
│   └── config.py          # Settings and config
│
├── migrations/            # Alembic migrations (if used)
├── tests/                  # Unit / integration tests
├── requirements.txt
└── README.md

Running Tests

If you have tests:

pytest


Include test coverage, fixtures, mock DB, etc.

Contributing

Fork the repo

Create a feature branch (git checkout -b feature/xyz)

Make changes & write tests

Commit with descriptive message

Push & open a Pull Request

License

Specify license (MIT, Apache, etc.).
