from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app= FastAPI()


@app.get('/')
def Home():
    return {"Detail":"Ankit"}


@app.get('/about')
def about():
    return {"Detail":"Ankit is a software engineer"}



@app.get('/blog/unpublish')
def unpublish():
    return {"Unpublish":"unpublish blog"}

# fatch blog with id
@app.get('/blog/{id}')
def blog(id:int):
    return {"id": id, "title": "Sample Blog Post"}

#fatch comment based on id
@app.get("/blog/{id}/comment")
def comment(id:int):
    return {"id": id, "content": "This is a comment"}


##Query parameter###########################################
#http://127.0.0.1:8000/blog?limit=10&publish=false
# query parameter to get the limit
# for default value we need to make like
# if we want to sort anything but that is  optional
# so using optionl need to import from typing  ,                    from typing import optional
# def blog(limit=10,publish:bool=True,sort:Optional[str]=None):
#     if publish==True:
#         return {"Limit": limit, "Blog":"List of Blogs"}
#     else:
#         return {"Limit": limit, "Blog":"List of Unpublish Blogs"}

# @app.get("/blog")
# def blog(limit,publish:bool):
#     if publish==True:
#         return {"Limit": limit, "Blog":"List of Blogs"}
#     else:
#         return {"Limit": limit, "Blog":"List of Unpublish Blogs"}
    

    #### Requeest body########################

# for body we need to import basemodal from pydantic

class Blog(BaseModel):
    title:str
    body:str
    publised:Optional[bool]

@app.post("/blog")
def blog(request:Blog):
    return request



# if we want to change the port on the server
# first import uvicorn

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
    