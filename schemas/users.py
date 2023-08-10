from pydantic import BaseModel, EmailStr
from fastapi.security import HTTPBasicCredentials


class UserCreate(BaseModel):
    email : EmailStr
    password: str
    fullname: str


class UserUpdate(BaseModel):
    password: str
    fullname : str


class UserSignIn(HTTPBasicCredentials):

     class Config:
        schema_extra = {
            "example": {"username": "user@darix.com", "password": "darix"}
        }

    