from datetime import datetime, timedelta

import bcrypt
from jose import jwt
from fastapi import Depends

from src.database.orm import User
from src.database.repository import UserRepository
from src.security import get_access_token


class UserService:
    encoding = "utf-8"
    secrete_key = "secret3232DSAG#3gdw35@GDQA#%"

    def __init__(self, user_repository: UserRepository = Depends(UserRepository)):
        self.user_repository = user_repository

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(self.encoding), bcrypt.gensalt()).decode(self.encoding)

    def sign_up(self, user: User) -> User:
        user = self.user_repository.sign_up(user)
        return user

    def get_user(self, username: str) -> User | None:
        user = self.user_repository.get_user(username)
        return user

    def check_password(self, req_password, db_password) -> bool:
        return bcrypt.checkpw(req_password.encode(self.encoding), db_password.encode(self.encoding))

    def create_jwt_token(self, username: str) -> dict[str, str]:
        token = jwt.encode(
            claims={
                "sub": username,
                "exp": datetime.now() + timedelta(minutes=30)
            },
            key=self.secrete_key,
            algorithm="HS256")
        return {"token": token}

    def get_user_by_access_token(self, access_token: str) -> User:
        payload = jwt.decode(access_token, self.secrete_key, algorithms=["HS256"])
        username = payload.get("sub")
        user = self.get_user(username)
        return user
