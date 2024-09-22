from pydantic import BaseModel, ConfigDict
from app.api.schemas.roles import Role


class UserLogin(BaseModel):
    username: str
    password: str


class UserRegistration(UserLogin):
    role: Role = Role.guest.value


class UserFromDB(UserLogin):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    role: Role


class User(BaseModel):
    user_id: int
    username: str
    role: Role


class Payload(BaseModel):
    username: str
    role: Role | str
    exp: float

    model_config = ConfigDict(from_attributes=True)