from fastapi import FastAPI

app= FastAPI()


@app.get('/')
def Home():
    return {"name":"Ankit"}