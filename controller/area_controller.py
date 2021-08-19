from fastapi import APIRouter
from model.area_model import AreaModel
from config import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

area_route = APIRouter(
    prefix="/area",
    tags=["area"]
)


@area_route.post("", response_description="Add new area", response_model=AreaModel)
async def create_area(area: AreaModel):
    area_model = jsonable_encoder(area)
    new_area = await db["area"].insert_one(area_model)
    return_area = await db["area"].find_one({"_id": new_area.inserted_id})
    return JSONResponse(content=return_area)


@area_route.get("", response_description="return 15 areas", response_model=List[AreaModel])
async def get_areas():
    areas = await db["area"].find().to_list(15)
    return areas
