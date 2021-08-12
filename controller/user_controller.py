from fastapi import APIRouter, status, Body
from model.user_model import UserModel, UserDto
from config import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from dto.message import Message

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


@user_route.get("", response_description="list of 15 users", response_model=List[UserModel])
async def list_users():
    users = await db["user_example"].find().to_list(15)
    return users


@user_route.get("/{id}", response_description="get user by id", response_model=UserModel)
async def get_user(id: str):
    if (user := await db["user_example"].find_one({"_id": id})) is not None:
        return user
    return JSONResponse(
        content=jsonable_encoder(Message(message='usuario no encontrado')),
        status_code=status.HTTP_404_NOT_FOUND,
        media_type="application/json"
    )


@user_route.put("/{id}", response_description="usuario modificado", response_model=Message)
async def update_user(id: str, user: UserDto = Body(...)):
    user_insert = {key: value for key, value in user.dict().items() if value is not None}
    if (user_help := await db["user_example"].find_one({"_id": id})) is not None:
        await db["user_example"].update_one({"_id": id}, {"$set": user_insert})
        return JSONResponse(
            content=jsonable_encoder(Message(message='usuario modificado')),
            status_code=status.HTTP_202_ACCEPTED,
            media_type="application/json"
        )
    return JSONResponse(
        content=jsonable_encoder(Message(message='usuario no encontrado')),
        status_code=status.HTTP_404_NOT_FOUND,
        media_type="application/json"
    )


@user_route.delete("/{id}", response_description="usuario eliminado", response_model=Message)
async def delete_user(id: str):
    if (user := await db["user_example"].find_one({"_id": id})) is not None:
        await db["user_example"].delete_one({"_id": id})
        return JSONResponse(
            content=jsonable_encoder(Message(message='usuario elimnado')),
            status_code=status.HTTP_202_ACCEPTED,
            media_type="application/json"
        )
    return JSONResponse(
        content=jsonable_encoder(Message(message='usuario no encontrado')),
        status_code=status.HTTP_404_NOT_FOUND,
        media_type="application/json"
    )
