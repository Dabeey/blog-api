from fastapi import APIRouter, FastAPI, Depends
from schemas import BlogSchema, ShowBlog
from models import Blog
from database import SessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()
app = FastAPI()


@router.get('/blog', response_model=List[ShowBlog], tags=['blogs'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

