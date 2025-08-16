from pydantic import BaseModel
from datetime import datetime
from fastapi import Depends
from .Users_Scheme import Responseuser




# Pydantic models
class PostSchema(BaseModel):
    title: str
    content: str
    published: bool = True
    
    

class PostResponseSchema(PostSchema):
    id: int
    created_at:datetime
    likes: int
    owner:Responseuser
    

    class Config:
        from_attributes = True

class Posts_Scheme_Response(PostSchema):
    id:int
    owner_id:int
    
    class Config:
        from_attributes = True
    
    
        


class PostVote(BaseModel):
    postId :int
    dir : bool = True,False
    