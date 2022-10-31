from pydantic import BaseModel


class UserPostRequestSchema(BaseModel):
    id: int


class UserSchema(UserPostRequestSchema):
    name: str
    department: str
    auth: int
