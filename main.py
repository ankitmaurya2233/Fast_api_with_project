from fastapi import FastAPI

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