from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Relationship
from .database import Base

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='true')  # Corrected to 'true' as a string for SQL compatibility
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable= False)
    owner = Relationship("User")
     
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
   
    
class Vote(Base):
    __tablename__ ="votes"
    user_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id =  Column(Integer,ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True,)
    
    
    
    