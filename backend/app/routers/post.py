from fastapi import FastAPI, HTTPException, Depends, status,APIRouter
from typing import Optional
from .. import model
from ..Posts_Scheme import PostSchema,PostResponseSchema,Posts_Scheme_Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..aoth2 import get_current_user
from..Users_Scheme import TokenData
from sqlalchemy import func

router = APIRouter(prefix="/posts",tags=["Posts"])

# Create a new post
@router.post("/", response_model=Posts_Scheme_Response, status_code=status.HTTP_201_CREATED)
def create_post(post: PostSchema, db: Session = Depends(get_db),current_user:int = Depends(get_current_user)):
    
    
    print(current_user.id)
    
    new_post = model.Post(owner_id = current_user.id,**post.dict())  
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/", response_model=list[PostResponseSchema])
def get_posts(db: Session = Depends(get_db), limit: int = 22, skip: int = 0, search: Optional[str] = ""):
    post_query = db.query(
        model.Post,
        func.count(model.Vote.post_id).label("likes")
    ).join(
        model.Vote, model.Vote.post_id == model.Post.id,isouter= True
    ).outerjoin(
        model.User, model.User.id == model.Post.owner_id
    ).group_by(
        model.Post.id, model.User.id
    ).filter(
        model.Post.title.contains(search)
    ).limit(limit).offset(skip).all()
    
    posts = []
    for post, likes in post_query:
        post_dict = post.__dict__.copy()
        post_dict['likes'] = likes
        post_dict['owner'] = {
            'id': post.owner.id,
            'username': post.owner.username,
            'email': post.owner.email
        }
        posts.append(PostResponseSchema(**post_dict))
    
    return posts

    
  
    
    

  

@router.get("/{id}", response_model=PostResponseSchema)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    post_result = db.query(
        model.Post, func.count(model.Vote.post_id).label("likes")
    ).join(
        model.Vote, model.Vote.post_id == model.Post.id, isouter=True
    ).group_by(
        model.Post.id
    ).filter(
        model.Post.id == id
    ).first()

    if not post_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

    post, likes = post_result
    post_dict = post.__dict__.copy()
    post_dict['likes'] = likes

    # Ensure owner data is included
    owner = post.owner
    post_dict['owner'] = {
        'id': owner.id,
        'username': owner.username,
        'email': owner.email
    }

    return PostResponseSchema(**post_dict)

    

# Delete a post by ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    post = db.query(model.Post).filter(model.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail= "Not Authorised to delete this post!")
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}

# Update a post by ID
@router.put("/{id}", response_model=PostResponseSchema)
def edit_post(id: int, post: PostSchema, db: Session = Depends(get_db), current_user:int = Depends(get_current_user)):
    existing_post = db.query(model.Post).filter(model.Post.id == id).first()
    if not existing_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    if existing_post.owner_id!= current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail= "Not Authorised to delete this post!")
        
    for key, value in post.dict().items():
        setattr(existing_post, key, value)
    db.commit()
    db.refresh(existing_post)
    return existing_post
