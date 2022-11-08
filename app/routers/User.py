from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException

from app.schemas.pydantic.User import UserSchema
from app.services.UserService import UserService

UserRouter = APIRouter(
    prefix="/user", tags=['user']
)


@UserRouter.get("/{id}", response_model=UserSchema)
def get(id: int, userService: UserService = Depends()):
    try:
        return userService.get(id).normalize()
    finally:
        return HTTPException(status_code=500, detail="Internal Server Error")
