from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import repository
from src.database.connection import get_db
from src.scheme.response import ListBase, TodoBase

router = APIRouter()


@router.get("/todos", status_code=200)
async def get_todos(
        order: str | None = None,
        todo_repository: repository.TodoRepository = Depends(repository.TodoRepository),
) -> ListBase:
    todos = todo_repository.get_todos()
    if order == "desc":
        todos = todos[::-1]

    return ListBase(todos=[TodoBase.from_orm(todo) for todo in todos])
