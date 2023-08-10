from fastapi import APIRouter, Body
from fastapi.exceptions import HTTPException
from models.user import UserNode
from database.database import initiate_database
from schemas.users import UserSignIn
from auth.jwt_handler import sign_jwt
from models.user import find_user_with_email

from passlib.context import CryptContext

UserRouter = APIRouter()


hash_helper = CryptContext(schemes=["bcrypt"])


@UserRouter.post("")
def add_new_user(user: UserNode):
    user_exists = user.match(user.email)
    if user_exists:
        raise HTTPException(
            status_code=409, detail="User with email supplied already exists"
        )
    user.password = hash_helper.encrypt(user.password)
    user.create()
    return user


@UserRouter.post("/token")
def user_get_token(user_credentials: UserSignIn = Body(...) ):
    
    user_exist = UserNode.match(user_credentials.username)

    if user_exist:

        password = hash_helper.verify(user_credentials.password, user_exist.password)
        if password:
            return sign_jwt(user_id=user_credentials.username)
        
        raise HTTPException(status_code=403, detail="Incorrect email or password")
    
    raise HTTPException(status_code=403, detail="Incorrect email or password")
    

