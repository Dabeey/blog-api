from pydantic import BaseModel

class BlogSchema(BaseModel):
    title: str
    body: str

class ShowBlog(BlogSchema):
    class Config():
        from_attributes = True


class UserSchema(BaseModel):
    name:str
    email : str
    password: str

