from fastapi import APIRouter, Depends, status, HTTPException
from models.post import PosteNode, Posted
from fastapi import Request
from typing import List
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import decode_jwt
from fastapi.exceptions import HTTPException
from models.user import UserNode
from models.post import Posted
from schemas.posts import PostCreate
from datetime import datetime

PostRouter = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_current_user(request: Request):
    pass

@PostRouter.post("")
def add_new_post(post: PostCreate, token = Depends(oauth2_scheme)):

    user_exists = decode_jwt(token=token)

    if not user_exists:
        raise HTTPException(status_code=403, detail= f"invalide token  credentials")
    
    users_exist = UserNode.match(user_exists.get("email"))
    

    if not users_exist:
        raise HTTPException(status_code=403, detail= "invalide token credentials")
    
    post_created = PosteNode(title=post.title, tags=post.tags,content=post.content, date_updated=datetime.now())
    post = post_created.create()

    posted = Posted(source=users_exist, target=post)
    posted.merge()


    return HTTPException(status_code=status.HTTP_201_CREATED, detail="post successfully created")


@PostRouter.get("")
def get_all_post(token = Depends(oauth2_scheme))->List[PosteNode]:
    user = decode_jwt(token=token)

    if not user:
        raise HTTPException(status_code=403, detail= "invalide token  credentials")
    
    users_exist = UserNode.match(user.get("email"))


    if not users_exist:
        raise HTTPException(status_code=403, detail= "invalide token  credentials")

    print(PosteNode.match_nodes())
    return PosteNode.match_nodes()
