from fastapi import APIRouter, Body, status, Depends
from fastapi.exceptions import HTTPException
from models.user import UserNode
from database.database import initiate_database
from schemas.users import UserSignIn, Token
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import sign_jwt
import logging
from passlib.context import CryptContext
from jwt import PyJWTError
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
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="user successfully created")


@UserRouter.post("/token")
def user_get_token(user_credentiel: OAuth2PasswordRequestForm = Depends() ):
    
    user_exist = UserNode.match(user_credentiel.username)

    if user_exist:

        try:
             
             password = hash_helper.verify(user_credentiel.password, user_exist.password)

        except PyJWTError as e:
            print(f"Exception {e}")
            logging.error(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

        except Exception as e:
            print(f"Exception {e}")
            logging.error(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Could not validate credentials",headers={"WWW-Authenticate": "Bearer"})


       
        if password:
            return sign_jwt(email=user_credentiel.username)
        
        raise HTTPException(status_code=403, detail="Incorrect email or password")
    
    raise HTTPException(status_code=403, detail="Incorrect email or password")
    

