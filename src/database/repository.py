from contextlib import contextmanager
from typing import List, Sequence

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.connection import session_scope, get_db
from src.database.orm import Todo, User


class TodoRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def get_todos(self) -> Sequence[Todo]:
        stmt: select = select(Todo)
        result = (
            self.session.scalars(stmt)
        ).all()
        # result text
        return result


class UserRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def sign_up(self, user: User) -> "User":
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user(self, username):
        stmt: select = select(User).where(User.username == username)
        result = (
            self.session.scalars(stmt)
        ).first()
        return result
