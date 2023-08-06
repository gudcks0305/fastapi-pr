from contextlib import contextmanager

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=True)
    is_done = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f"<Todo {self.id} {self.contents} {self.is_done}>"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), nullable=True)
    password = Column(String(256), nullable=True)
    todos = relationship("Todo", lazy="joined")

    def __repr__(self):
        return f"<User {self.id} {self.name} {self.email} {self.password}>"

    @classmethod
    def create(cls, name: str, hashed_password: str) -> "User":
        return cls(username=name, password=hashed_password)