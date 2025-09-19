from fastapi import FastAPI, Depends, status, Response, HTTPException
from schemas import BlogSchema, ShowBlog, UserSchema
from models import Blog, User
from database import Base,engine, SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext


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
    db.refresh()
    return new_blog


@app.get('/')
def all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=200, response_model = ShowBlog)
def show(id: int, response:Response, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).delete(synchronize_session=False)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
    
    db.commit()
    return f'Deleted blog with id {id}'


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: BlogSchema, db: Session = Depends(get_db) ):

    blog  = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
    
    blog.update(request.dict())
    db.commit()
    return f'Updated blog with id {id}'




@app.post('/user')
def create_user(request:UserSchema, db: Session = Depends(get_db)):
    # hashed_password = pwd_cxt.hash(request.password)
    new_user = User(name = request.name, email = request.email, password = request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user