from fastapi import FastAPI
from internal import admin

app = FastAPI()

app.include_router(admin.router)
