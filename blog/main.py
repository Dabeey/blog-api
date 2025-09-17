from fastapi import FastAPI, Depends
from schemas import BlogSchema
from models import Base, Blog
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


@app.post('/blog')
def create(request:BlogSchema, db: Session = Depends(get_db) ):
    new_blog = Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

