from fastapi import FastAPI, Request, Response, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.user import User as Usuario
from lib.check_passw import check_user
from lib.check_passw import check_user2
from model.handle_db import HandleDB

from typing import Optional
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()




origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class User(BaseModel):
    username: str
    password: str

class data_User(BaseModel):
    firstname: str
    lastname: str
    username: str
    country: str
    password_user: str

class Settings(BaseModel):
    authjwt_secret_key: str = "my_jwt_secret"

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@app.post('/login')
def login(req: Request, user: User, Authorize: AuthJWT = Depends()):
    print(user.username)
    print(user.password)
    verify = check_user(user.username, user.password)
    if verify:
        access_token = Authorize.create_access_token(subject=user.username)
        return {"access_token": access_token,"data_user":verify}
    return False

@app.post("/dataProcessingA")
def dataProcessingA(req: Request,dataUser: data_User):
    print(dataUser)
    data_user1={
        "firstname": dataUser.firstname,
        "lastname": dataUser.lastname,
        "username": dataUser.username,
        "country": dataUser.country,
        "password_user": dataUser.password_user
    } 
    
    print(data_user1)
    db = Usuario(data_user1)
    db.create_user()
    return True

@app.post("/user2")
def user2(req: Request, user:User):

    verify = check_user2(user.username)
    if verify:
        return {"data_user": verify}
    return None

@app.get("/list-users")
def listUsers(req: Request):
    users=HandleDB()
    list=users.get_all()
    print(list)
    return list

