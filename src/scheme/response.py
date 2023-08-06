from typing import List

from pydantic import BaseModel


class TodoBase(BaseModel):
    id: int
    contents: str
    is_done: bool

    class Config:
        orm_mode = True
        from_attributes = True


class ListBase(BaseModel):
    todos: List[TodoBase]


class UserModel(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
        from_attributes = True
