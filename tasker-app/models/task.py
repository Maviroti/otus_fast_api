from models.base import Base
from models.mixins.created_at import CreatedAtMixin
from models.mixins.id_int_pk import IdIntPkMixin

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime


class Task(IdIntPkMixin, CreatedAtMixin, Base):
    title: Mapped[str] = mapped_column(
        String(150),
    )
    user_name: Mapped[str] = mapped_column(
        String(100),
        default="",
        server_default="",
    )
    body: Mapped[str] = mapped_column(
        String(500),
        default="",
        server_default="",
    )
    end_date: Mapped[datetime] = mapped_column(
        DateTime,
    )
