from fastapi import FastAPI, Depends, status, Response, HTTPException
from .schemas import BlogSchema, ShowBlog, UserSchema, ShowUser
from .models import Blog, User
from .database import Base,engine, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .hashing import Hash
from typing import List
from .routers import blog


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(blog.router)


# @app.post('/blog',status_code=status.HTTP_201_CREATED, response_model = ShowBlog, tags=['blogs'] )
# def create(request:BlogSchema, db: Session = Depends(get_db) ):
#     new_blog = Blog(title = request.title, body = request.body, user_id = 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


@app.post('/user', response_model=ShowUser, tags=['user'])
def create_user(request:UserSchema, db: Session = Depends(get_db)):
    new_user = User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@app.get('/users/{id}', status_code=200, response_model=ShowUser, tags=['user'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found.')
    return user