from pydantic import BaseModel


class Manager(BaseModel):
    name: str
    email: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com"
            }
        }
