from pydantic import BaseModel, EmailStr
from typing import List



class PostCreate(BaseModel):
    title : str
    content: str
    tags: List[str]


    