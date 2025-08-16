from fastapi import FastAPI, HTTPException, Depends, status,APIRouter
from typing import Optional
from .. import model
from ..Posts_Scheme import PostSchema,PostResponseSchema,PostVote
from sqlalchemy.orm import Session
from ..database import get_db
from ..aoth2 import get_current_user


router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)
#  the edge cases or every scenario that can make my application work effeciently yoo!
@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote:PostVote,db:Session = Depends(get_db), current_user:int=Depends(get_current_user)):
    
    post =db.query(model.Post).filter(model.Post.id == vote.postId).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="posts does not exist!")
    
    votes = db.query(model.Vote).filter( vote.postId == model.Vote.post_id,model.Vote.user_id ==current_user.id)
    votefound = votes.first()
    
    if vote.dir == True:
        if votefound:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"current {current_user.id}  has Vote Already ")
        
        
        new_vote = model.Vote(post_id =vote.postId,user_id =current_user.id)
        db.add(new_vote)
        db.commit()  
        return {"message":"vote successfully created"}
    
    elif vote.dir== False:
        if  not votefound:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Vote deos not exists")
        
        
        
        db.delete(votes)
        db.commit()  
        
        return{"message":"vote successfully deleted"}
        
        