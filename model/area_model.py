from pydantic import BaseModel, Field
from model.PyObjectId import PyObjectId
from bson import ObjectId
from model.user_model import UserDto
from model.manager_model import Manager
from typing import List


class AreaModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    code: str = Field(...)
    users: List[UserDto] = Field(...)
    manager: Manager

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Software",
                "code": "sft",
                "manager": {
                    "name": "Jane Doe",
                    "email": "jdoe@example.com"
                },
                "users": [
                    {
                        "name": "Jane Doe",
                        "email": "jdoe@example.com",
                        "password": "adfa123123adfafd"
                    }
                ]
            }
        }
