from pydantic import BaseModel


class Tag(BaseModel):
    id: int
    name: str


class City(BaseModel):
    id: int
    name: str
    population: int
    tags: list[Tag]
