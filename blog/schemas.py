from pydantic import BaseModel

class BlogSchema(BaseModel):
    title: str
    body: str
    



class UserSchema(BaseModel):
    name:str
    email : str
    password: str


class ShowUser(UserSchema):
    name:str
    email : str

    class Config():
        from_attributes = True


class ShowBlog(BlogSchema):
    title: str
    body: str

    creator: ShowUser

    class Config():
        from_attributes = True
