from fastapi import APIRouter, Depends, HTTPException, status
from ..schemas import Login
from sqlalchemy.orm import Session
from ..models import User
from ..database import get_db
from ..hashing import Hash
from ..token import create_access_token

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: Login, db:Session = Depends(get_db) ):
    user = db.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Email')
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect Password')
    
    # Generate a jwt and return
    access_token = create_access_token(data = {'sub': user.email})
    return {'access_token': access_token, 'token_bearer': 'bearer'}