from fastapi import FastAPI

# create an instance
app = FastAPI()

# create a simple python function
#  Use decorater
@app.get('/')
def index():
    return {'data': {'name': 'Dabeey'}}

#  create route '/about'
@app.get('/about')
def about():
    return {'data':'about page'}