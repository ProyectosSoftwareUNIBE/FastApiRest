from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPBearer
from config import basic_authentication, bearer_authentication
from datetime import datetime, timedelta
import jwt

auth_route = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@auth_route.get("/basic_beginning")
def read_with_basic_beginning(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    return {"username": credentials.username, "password": credentials.password}


@auth_route.get("/basic")
def read_with_basic(username: str = Depends(basic_authentication)):
    return {"username": username}


@auth_route.post("/bearer")
def create_jwt(user: str = Depends(basic_authentication)):
    expire = datetime.utcnow() + timedelta(minutes=60)
    encoded_jwt = jwt.encode({'sub': user, 'exp': expire}, 'secret_key-Y0eT145', algorithm='HS256')
    return {"token": encoded_jwt}


@auth_route.get("/bearer")
def read_with_jwt(user: str = Depends(bearer_authentication)):
    return {"username": user}
