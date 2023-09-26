from fastapi import APIRouter, Depends, status, HTTPException
from models.post import PosteNode, Posted
from fastapi import Request
from typing import List
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import decode_jwt
from fastapi.exceptions import HTTPException
from models.user import UserNode
from models.post import Posted
from schemas.posts import PostCreate, PostUpdate
from datetime import datetime
from uuid import UUID
from auth.deps import get_current_user

PostRouter = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

@PostRouter.post("", status_code=status.HTTP_201_CREATED, )
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
    return post


@PostRouter.get("")
def get_all_post(token = Depends(oauth2_scheme))->List[PosteNode]:
    user = decode_jwt(token=token)

    if not user:
        raise HTTPException(status_code=403, detail= "invalide token  credentials")
    
    users_exist = UserNode.match(user.get("email"))


    if not users_exist:
        raise HTTPException(status_code=403, detail= "invalide token  credentials")

    return PosteNode.match_nodes()

@PostRouter.put("/{post_uuid}")
def update_post(post_uuid: str, post_update: PostUpdate, user: UserNode = Depends(get_current_user)):

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    
    post = PosteNode.match(post_uuid)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The POST does not exist")
    
    post.title = post_update.title
    post.content = post_update.content
    post.tags = post_update.tags
    post.merge()

    return HTTPException(status_code=status.HTTP_200_OK, detail=f"User with {post_uuid} was updating")

@PostRouter.delete("/{post_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_uuid: str, user: UserNode = Depends(get_current_user)):

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    
    PosteNode.delete(post_uuid)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"User with {post_uuid} was deleting")

