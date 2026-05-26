#main_model.py

from __future__ import annotations

from sqlalchemy import DateTime 

from main_database import Base

from datetime import UTC, datetime

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

class ShortURL(Base):
    __tablename__ = "data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    url: Mapped[str] = mapped_column(nullable=False)
    code: Mapped[str] = mapped_column(nullable=False)
    click_cnt: Mapped[int] = mapped_column(default=0, nullable=False)
    date_posted: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
