from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app= FastAPI()

class Post(BaseModel):
    title:str
    content:str


@app.get("/")
def read():
    return {"hello":"world"}

@app.get("/posts")
def get_posts():
    return{"Data: This is your posts"}

@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post.title)
    print(new_post.content)
    return{"data":"new post"}
