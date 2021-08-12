from fastapi import APIRouter
from model.user_model import UserModel, UserDto
from config import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

user_route = APIRouter(
    prefix="/user",
    tags=["user"]
)


@user_route.post("", response_description="Add new User", response_model=UserModel)
async def create_user(user: UserDto):
    user_model = UserModel(name=user.name, email=user.email, password=user.password)
    user_json = jsonable_encoder(user_model)
    new_user = await db["user_example"].insert_one(user_json)
    insert_user = await db["user_example"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(content=insert_user)
