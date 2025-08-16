from fastapi import FastAPI, HTTPException, Depends, status,APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from .. import model,aoth2
from sqlalchemy.orm import Session
from ..database import get_db
from ..Users_Scheme  import  Access_Token
from ..utils import verify 



router = APIRouter(tags=["Authentication"])



@router.post("/login", status_code=status.HTTP_200_OK,response_model=Access_Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect username or password")
    
    if not verify(user.password, User.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect username or password")
    
    access_token = aoth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "Bearer"}



