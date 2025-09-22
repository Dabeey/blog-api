from fastapi import APIRouter, FastAPI, Depends, status
from ..schemas import BlogSchema, ShowBlog
from ..models import Blog
from ..database import SessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()
app = FastAPI()


@router.get('/blog', response_model=List[ShowBlog], tags=['blogs'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@app.post('/blog',status_code=status.HTTP_201_CREATED, response_model = ShowBlog, tags=['blogs'] )
def create(request:BlogSchema, db: Session = Depends(get_db) ):
    new_blog = Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
