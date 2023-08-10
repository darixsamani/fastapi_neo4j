from pydantic import BaseModel, EmailStr
from typing import List



class PostCreate(BaseModel):
    title : EmailStr
    content: str
    tags: List[str]


class PostCreate(BaseModel):
    title : EmailStr
    content: str
    tags: List[str]


    