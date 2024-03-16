from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated

from typing import Optional
from datetime import datetime

# Schema/Pydantic model
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostCreate(PostBase):
    pass

# Pydantic response schema
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

# Data embedded into our access token
class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(strict=True, le=1)]