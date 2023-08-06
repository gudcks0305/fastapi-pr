from pydantic import BaseModel


class SignUpRequest(BaseModel):
    username: str
    password: str


class LogInRequest(BaseModel):
    username: str
    password: str
