from fastapi import APIRouter, FastAPI, Depends, status, HTTPException
from ..schemas import BlogSchema, ShowBlog
from ..models import Blog
from ..database import SessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
from ..repositories import blog, user


router = APIRouter(
    prefix='/blog',
    tags = ['Blogs']
)

app = FastAPI()


@router.get('', response_model=List[ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.post('',status_code=status.HTTP_201_CREATED, response_model = ShowBlog )
def create(request:BlogSchema, db: Session = Depends(get_db) ):
    return blog.create_blog(request, db)


@router.get('/{id}', status_code=200, response_model = ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog.show_blog(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return blog.delete_blog(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED,response_model = ShowBlog)
def update(id: int, request: BlogSchema, db: Session = Depends(get_db) ):
    return blog.update_blog(id, request, db)