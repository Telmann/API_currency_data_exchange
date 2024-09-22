from pydantic import BaseModel
from enum import Enum


class Role(Enum):
    guest = 'guest'
    user = 'user'
    admin = 'admin'