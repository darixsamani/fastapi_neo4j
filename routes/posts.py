from fastapi import APIRouter, Depends
from models.post import PosteNode, Posted
from fastapi import Request
from typing import List
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import decode_jwt
from fastapi.exceptions import HTTPException
from models.user import UserNode
from models.post import Posted

PostRouter = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

def get_current_user(request: Request):
    pass

@PostRouter.post("")
def add_new_post(post: PosteNode, token = Depends(oauth2_scheme)):

    user_exists = decode_jwt(token=token)

    if not user_exists:
        raise HTTPException(status_code=403, detail= f"invalide token  credentials")
    
    users_exist = UserNode.match(user_exists.get("email"))
    

    if not users_exist:
        raise HTTPException(status_code=403, detail= "invalide token credentials")
    

    post = post.create()

    posted = Posted(source=users_exist, target=post)
    posted.merge()


    return post


@PostRouter.get("")
def get_all_post(requesst : Request, token = Depends(oauth2_scheme))->List[PosteNode]:
    user_exists = decode_jwt(token=token)

    if user_exists:
        raise HTTPException(status_code=403, detail= "invalide token  credentials")
    
    users_exist = UserNode.match(email=user_exists.get("email"))

    if user_exists:
        raise HTTPException(status_code=403, detail= "invalide token  credentials")


    return PosteNode.match_nodes()
