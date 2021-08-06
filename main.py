from fastapi import FastAPI
import uvicorn
from Dtos.Dto import Dto
from Dtos.Message import Message
from fastapi.openapi.utils import get_openapi
from typing import List
import fastapi

app = FastAPI(name="example")


@app.get("/dto", response_model=List[Dto])
def find() -> [Dto]:
    return [Dto(id='1', name='intel i9', description='procesador de 8 nucleos y 16 hilos')]


@app.get("/dto/{ide}", response_model=Dto)
def findOne(ide: str) -> Dto:
    return Dto(id=ide, name="dto", description='desc')


@app.post("/dto", responses={202: {"model": Message}})
def create(dto: Dto) -> fastapi.responses:
    return fastapi.responses.JSONResponse(
        content={'message': 'dto creado'},
        status_code=202,
        media_type="application/json"
    )


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Exjemplo",
        version="0.0.1",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80, access_log=True)
