from pydantic  import BaseModel,EmailStr
from datetime import datetime
from typing import Optional


class PostUser(BaseModel):
    email:EmailStr
    username:str
    password: str
    
    
class Responseuser(BaseModel):
     id:int
     username:str
     email : EmailStr
     
   
     class Config:
        from_attributes = True
        
        

class Authentication(BaseModel):
    email:EmailStr
    password:str

class Access_Token(BaseModel):
    access_token :str
    token_type:str
    
class TokenData(BaseModel):
    id: int

    class Config:
        from_attributes = True