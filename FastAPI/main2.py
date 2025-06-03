# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel
# import uvicorn

# app = FastAPI()


# #GET Requests
# @app.get("/blog")
# def index(limit=10, published: bool=True, sort: Optional[str] = None):
#     if published:
#         return {'data': f'{limit} published blogs'}
#     else:
#         return {'data': f'{limit} unpublished blogs'}

# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data': "All unpublished blogs"}


# @app.get('/blog/{id}')
# def about(id: int):
#     return {'data': id}


# @app.get('/blog/{id}/comments')
# def comments(id, limit=10):
#     return limit

# #Model class
# class Blog(BaseModel):
#     title: str
#     body: str
#     published: Optional[bool]


# #POST Requests
# @app.post('/blog')
# def create_blog(blog: Blog):
#     return {'data': f"Blog is created with title {blog.title}"}
    
    
# # For debugging
# # if __name__ == "__main__":
# #     uvicorn.run(app, host='127.0.0.1', port=9000)