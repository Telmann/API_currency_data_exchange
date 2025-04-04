from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String, ForeignKey

from app.database.db import Base


class Role(Base):
    __tablename__ = 'roles'

    role: Mapped[str] = mapped_column(String, primary_key=True, nullable=False)


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True, autoincrement=True)
    username: Mapped[str]
    password: Mapped[str]
    role: Mapped[str] = mapped_column(ForeignKey(Role.role))

    @staticmethod
    def get_primary_key():
        return User.user_id