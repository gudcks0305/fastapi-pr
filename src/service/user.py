import bcrypt
from fastapi import Depends

from src.database.orm import User
from src.database.repository import UserRepository


class UserService:
    encoding = "utf-8"

    def __init__(self, user_repository: UserRepository = Depends(UserRepository)):
        self.user_repository = user_repository

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(self.encoding), bcrypt.gensalt()).decode(self.encoding)

    def sign_up(self, user: User) -> User:
        user = self.user_repository.sign_up(user)
        return user
