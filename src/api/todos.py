from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import repository
from src.database.connection import get_db
from src.scheme.response import ListBase, TodoBase
from src.security import get_access_token

router = APIRouter()


@router.get("/todos", status_code=200)
async def get_todos(
        access_token: str = Depends(get_access_token),
        order: str | None = None,
        todo_repository: repository.TodoRepository = Depends(repository.TodoRepository),
) -> ListBase:
    print(access_token)
    todos = todo_repository.get_todos()
    print(todos)
    if order == "desc":
        todos = todos[::-1]

    return ListBase(todos=[TodoBase.from_orm(todo) for todo in todos])
