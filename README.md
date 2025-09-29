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
