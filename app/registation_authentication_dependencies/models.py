from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, ForeignKey
from datetime import datetime

from app.database.db import Base
from app.models.models import User


class Session(Base):
    __tablename__ = 'sessions'

    session_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, index=True)
    refresh_token: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey(User.user_id))
    fingerprint: Mapped[str]
    exp_at: Mapped[float]
    created_at: Mapped[datetime]

    @staticmethod
    def get_primary_key() -> int:
        return Session.session_id