from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from fortuhost.infrastructure.db.models.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(sa.Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(sa.DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(sa.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"
