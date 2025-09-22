from fastapi import FastAPI
from .database import Base,engine
from .routers import blog, user, authentication

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)