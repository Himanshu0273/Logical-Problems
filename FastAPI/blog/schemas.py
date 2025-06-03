from typing import List
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    class Config():
        from_attributes = True
    
    
class User(BaseModel):
    username: str
    email: str
    password: str
    
    
class ShowUser(BaseModel):
    username: str
    email: str
    blogs: List[Blog]=[]
    class Config():
        from_attributes = True
    
        
        
class ShowBlog(BaseModel):
    title: str
    body: str
    author: ShowUser
    class Config():
        from_attributes = True



class Login(BaseModel):
    username: str
    password: str

    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
