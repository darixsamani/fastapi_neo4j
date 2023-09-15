from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from auth.jwt_handler import decode_jwt
from models.user import UserNode

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def get_current_user(token: str = Depends(oauth2_scheme)):

    user = decode_jwt(token=token)
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

    user_exist = UserNode.match(user["email"])
    
    return user_exist

