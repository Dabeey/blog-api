from pydantic import BaseModel

class BlogSchema(BaseModel):
    title: str
    body: str

class ShowBlog(BlogSchema):
    class Config():
        orm_mode = True