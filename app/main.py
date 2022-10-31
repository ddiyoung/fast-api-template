from fastapi import FastAPI
from routers import User

app = FastAPI()

app.include_router(User.UserRouter)
