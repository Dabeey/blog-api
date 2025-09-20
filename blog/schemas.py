from pydantic import BaseModel

class BlogSchema(BaseModel):
    title: str
    body: str
    

class ShowBlog(BlogSchema):
    title: str
    body: str

    class Config():
        from_attributes = True


class UserSchema(BaseModel):
    name:str
    email : str
    password: str


class ShowUser(UserSchema):
    name:str
    email : str

    class Config():
        from_attributes = True