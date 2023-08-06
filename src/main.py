from fastapi import FastAPI
from src.api.todos import router as todos
from src.api.user import router as user
app = FastAPI()

app.include_router(todos)
app.include_router(user)
