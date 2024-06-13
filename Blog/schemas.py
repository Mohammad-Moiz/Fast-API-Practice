from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title : str
    body : str

class User(BaseModel):
    name : str
    email : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    username : Optional[str] = None

class ShowUser(BaseModel):
    name : str
    email : str
    password : str
    blog : list

    class Config():
        orm_mode = True

class ShowBlog(Blog):
    title : str
    body : str
    blog : list
    creator : ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username : str
    password : str
