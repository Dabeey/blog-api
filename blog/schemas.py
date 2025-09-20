from pydantic import BaseModel
from typing import List


class BlogSchema(BaseModel):
    title: str
    body: str


class UserSchema(BaseModel):
    name:str
    email : str
    password: str


class ShowUser(BaseModel):
    name:str
    email : str

    blogs: List[BlogSchema] = []

    class Config():
        from_attributes = True


class ShowBlog(BaseModel):
    title: str
    body: str

    creator: ShowUser

    class Config():
        from_attributes = True
