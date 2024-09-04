from fastapi import FastAPI
from . import schemas

# crud operation

app=FastAPI()




@app.post('/blog')
def create(request:schemas.Blog):
    return request