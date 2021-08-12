import fastapi
from fastapi import APIRouter
from dto.dto import Dto
from dto.message import Message
from typing import List

dto_route = APIRouter(
    prefix="/dto",
    tags=["dto"]
)


@dto_route.get("", response_model=List[Dto])
def find() -> [Dto]:
    return [Dto(id='1', name='intel i9', description='procesador de 8 nucleos y 16 hilos')]


@dto_route.get("/{ide}", response_model=Dto)
def findOne(ide: str) -> Dto:
    return Dto(id=ide, name="dto", description='desc')


@dto_route.post("", responses={202: {"model": Message}})
def create(dto: Dto) -> fastapi.responses:
    return fastapi.responses.JSONResponse(
        content={'message': 'dto creado'},
        status_code=202,
        media_type="application/json"
    )
