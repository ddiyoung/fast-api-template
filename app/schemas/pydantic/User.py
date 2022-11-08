from pydantic import BaseModel


class UserPostRequestSchema(BaseModel):
    user_id: str


class UserSchema(UserPostRequestSchema):
    user_name: str
    user_department: str
    user_auth: str
