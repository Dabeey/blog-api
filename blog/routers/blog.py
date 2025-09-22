from fastapi import APIRouter, FastAPI, Depends, status, HTTPException
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


@router.post('/blog',status_code=status.HTTP_201_CREATED, response_model = ShowBlog, tags=['blogs'] )
def create(request:BlogSchema, db: Session = Depends(get_db) ):
    new_blog = Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/blog', response_model=List[ShowBlog], tags=['blogs'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@router.get('/blog/{id}', status_code=200, response_model = ShowBlog, tags=['blogs'])
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
    return blog


@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).delete(synchronize_session=False)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
    
    db.commit()
    return f'Deleted blog with id {id}'


@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,response_model = ShowBlog,  tags=['blogs'])
def update(id: int, request: BlogSchema, db: Session = Depends(get_db) ):

    blog  = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
    
    blog.update(request.dict())
    db.commit()
    return f'Updated blog with id {id}'
