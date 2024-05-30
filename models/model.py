from pydantic import BaseModel

class User(BaseModel):
    name: str
    price: int
    decription: str


