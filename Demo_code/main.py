from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


# create an instance
app = FastAPI()

# create a simple python function
#  Use decorater
@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # only get n published blogs
    if published:
        return {'data': f'{limit} published blogs sorted by {sort} from the db'}
    else:
        return {'data': f'{limit} blogs sorted by {sort} from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'All unpublished blogs'}


#  create route '/about'
@app.get('/blog/{id}')
def show(id: int):
    return {'data':{id}}


@app.get('/blog/{id}/comments')
def comments(id:int, limit: Optional[int] = None):
    return {'data':{'1','2'}}



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'blog is created with title as {blog.title}'}



# if __name__ == '__main__':
#     uvicorn.run(app, host='', port=8000, debug=True)