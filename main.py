from fastapi import FastAPI
from typing import Optional
app = FastAPI()
from pydantic import BaseModel
@app.get("/blog")
def index(limit: int = 10, published: bool = True , ):
    return {
        "data": f"Displaying {limit} blogs",
        "published": published
    }

@app.get('/blog/unpuplished')
def unpublisshed():
    return {'data' : 'all unpublished blogs'}

@app.get('/blog/{id}')

def show(id : int ):
    # fetch blog with id = id 
    
    return {'data' : id}

@app.get('/blog/{id}/comments')

def comments(id):
    # fetch comment of blog with id = id 
    return {'data' : {1 , 2}}


class Blog(BaseModel):
    title : str 
    body : str 
    published : Optional[bool]
    




@app.post('/blog')
def create_blog(request : Blog):
    return {'data':f"Blog is created with {request.title}"} 