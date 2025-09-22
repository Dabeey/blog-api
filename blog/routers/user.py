from fastapi import APIRouter, FastAPI, Depends, status, HTTPException
from ..schemas import UserSchema, ShowUser
from ..models import User
from ..database import SessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
from ..hashing import Hash
from ..repositories import user

router = APIRouter(
    prefix='/user',
    tags = ['Users']
)

app = FastAPI()



@router.post('', response_model=ShowUser)
def create_user(request:UserSchema, db: Session = Depends(get_db)):
    return user.creat_user(request, db)



@router.get('/{id}', status_code=200, response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id,db)