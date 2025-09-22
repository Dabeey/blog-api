from pydantic import BaseModel
from typing import List, Optional


class BlogSchema(BaseModel):
    title: str
    body: str


class UserSchema(BaseModel):
    name:str
    email : str
    password: str


class Login(BaseModel):
    username : str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None




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
