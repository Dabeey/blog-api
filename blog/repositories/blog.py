from fastapi import HTTPException, status
from ..models import Blog
from sqlalchemy.orm import Session
from ..schemas import BlogSchema



def get_all(db : Session):
    blogs = db.query(Blog).all()
    return blogs


def create_blog(request: BlogSchema, db:Session):
    new_blog = Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
    return blog


def delete_blog(id:int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).delete(synchronize_session=False)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
    
    db.commit()
    return f'Deleted blog with id {id}'



def update_blog(id: int, request: BlogSchema, db: Session):
    blog  = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
    
    blog.update(request.model_dump())
    db.commit()
    return f'Updated blog with id {id}'
