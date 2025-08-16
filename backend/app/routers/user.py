from fastapi import FastAPI, HTTPException, Depends, status,APIRouter
from .. import model
from ..Users_Scheme import PostUser,Responseuser
from sqlalchemy.orm import Session
from ..utils import hash
from ..database import get_db


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/",response_model=Responseuser, status_code=status.HTTP_201_CREATED)
def create_user(user:PostUser, db: Session= Depends(get_db)):
    
    
    users = db.query(model.User).filter(model.User.email ==user.email,model.User.username ==user.username).first()
    if not users:
        hashed_password= hash(user.password)
        user.password = hashed_password
        new_user = model.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return new_user
    raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="already exits!")

    

@router.get("/{id}",response_model= Responseuser,status_code=status.HTTP_200_OK)
def  get_user(id:int,db: Session=Depends(get_db)):
    user = db.query(model.User).filter(model.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the user does not exist")
    return user
    
