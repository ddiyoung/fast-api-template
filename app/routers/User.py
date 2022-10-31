from typing import List, Optional
from fastapi import APIRouter, Depends, status

from schemas.pydantic.User import UserSchema
from services.UserService import UserService

UserRouter = APIRouter(
    prefix="/user", tags=['user']
)


@UserRouter.get("/{id}", response_model=UserSchema)
def get(id: int, userService: UserService = Depends()):
    return userService.get(id).normalize()
