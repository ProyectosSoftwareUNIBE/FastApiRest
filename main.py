from fastapi import FastAPI
import uvicorn
from fastapi.openapi.utils import get_openapi
from controller.dto_controller import dto_route
from controller.user_controller import user_route
from controller.area_controller import area_route
from controller.auth_controller import auth_route

app = FastAPI(name="example")
app.include_router(dto_route)
app.include_router(user_route)
app.include_router(area_route)
app.include_router(auth_route)


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
