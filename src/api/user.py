from fastapi import APIRouter, Depends

from src.database.orm import User
from src.scheme.request import SignUpRequest, LogInRequest
from src.scheme.response import UserModel
from src.service.user import UserService

router = APIRouter()


@router.post("/sign-up", status_code=200)
async def sign_up(request: SignUpRequest,
                  user_service: UserService = Depends(UserService),
                  ):
    hashed_password = user_service.hash_password(request.password)
    user = User.create(name=request.username, hashed_password=hashed_password)
    user = user_service.sign_up(user)
    return UserModel.model_validate(user)


@router.post("/log-in", status_code=200)
async def log_in(
        request: LogInRequest,
        user_service: UserService = Depends(UserService),
):
    user = user_service.get_user(request.username)
    if user is None:
        return {"message": "user not found"}
    if not user_service.check_password(request.password, user.password):
        return {"message": "password is incorrect"}
    return user_service.create_jwt_token(user.username)


