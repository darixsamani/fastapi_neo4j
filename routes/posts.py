from fastapi import APIRouter
from models.post import PosteNode, Posted


PostRouter = APIRouter()


@PostRouter.post("")
def add_new_post(post: PosteNode):
    pass