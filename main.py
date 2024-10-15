from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app= FastAPI()

class Post(BaseModel):
    title:str
    content:str

my_posts=[{"title":"Title of post1","content":"Content of post1","id":1},{"title":"Title of post2","content":"Content of post2","id":2}]

@app.get("/")
def read():
    return {"hello":"world!"}


@app.get("/posts")
def get_posts():
    return{"data":my_posts}

@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post.title)
    print(new_post.content)
    return{"data":"new post"}