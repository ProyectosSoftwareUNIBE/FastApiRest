import fastapi
from fastapi import FastAPI
import uvicorn
from Dtos.Dto import Dto

app = FastAPI(name="example")


@app.get("/dto")
def find() -> [Dto]:
    return [Dto(id='1', name='intel i9', description='procesador de 8 nucleos y 16 hilos')]


@app.post("/dto")
def create(dto: Dto) -> fastapi.responses:
    return fastapi.responses.JSONResponse(
        content={'message': 'dto creado'},
        status_code=202,
        media_type="application/json"
    )


@app.get("/dto/{ide}")
def findOne(ide: str) -> Dto:
    return Dto(id=ide, name="dto", description='desc')


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80, access_log=True)
