from database.database import initiate_database
# from routes.posts import  PostRouter
from routes.users import  UserRouter
from fastapi import FastAPI, Depends
from auth.jwt_bearer import JWTBearer
import logging

app = FastAPI()

token_listener = JWTBearer()

FORMAT = '%(levelname)s: %(asctime)-15s: %(filename)s: %(funcName)s: %(module)s: %(message)s'
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)


@app.on_event("startup")
async def start_database():
    initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(UserRouter, tags=["Administrator"], prefix="/users")
# app.include_router(PostRouter, tags=["Posts"], refix="/post", dependencies=[Depends(token_listener)],)