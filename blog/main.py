from fastapi import FastAPI, Depends, status
from schemas import BlogSchema
from models import Blog
from database import Base,engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request:BlogSchema, db: Session = Depends(get_db) ):
    new_blog = Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/')
def all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@app.get('/blog/{id}')
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog