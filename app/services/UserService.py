from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.UserModel import User
from repositories.UserRepository import UserRepository
from schemas.pydantic.User import UserSchema


class UserService:
    UserRepository: UserRepository

    def __init__(self, userRepository: UserRepository = Depends()) -> None:
        self.userRepository = userRepository

    def get(self, user_id: int) -> User:
        return self.userRepository.get(User(id=user_id))