from fastapi import APIRouter, FastAPI, Depends, status, HTTPException
from ..schemas import UserSchema, ShowUser
from ..models import User
from ..database import SessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
from ..hashing import Hash


router = APIRouter(
    prefix='/user',
    tags = ['Users']
)

app = FastAPI()



@router.post('', response_model=ShowUser)
def create_user(request:UserSchema, db: Session = Depends(get_db)):
    new_user = User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get('/{id}', status_code=200, response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found.')
    return user