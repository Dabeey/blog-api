from fastapi import Depends
from ..models import Blog
from sqlalchemy.orm import Session


def get_all(db : Session):
    blogs = db.query(Blog).all()
    return blogs
