from pydantic import BaseModel


class Dto(BaseModel):
    id: str
    name: str
    description: str
