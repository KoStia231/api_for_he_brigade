from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .worker import Worker


class Brigade(Base):
    __tablename__ = "brigades"

    name: Mapped[str] = mapped_column(String, nullable=False)

    # Связь с работниками
    workers: Mapped[list["Worker"]] = relationship("Worker", back_populates="brigade")

