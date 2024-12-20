from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Worker(Base):
    __tablename__ = "workers"

    full_name: Mapped[str] = mapped_column(String, nullable=False)
    salary: Mapped[float] = mapped_column(Float, nullable=False)
    specialization: Mapped[str] = mapped_column(String, nullable=False)
    brigade_id: Mapped[int | None] = mapped_column(ForeignKey("brigades.id"), nullable=True)

    # Связь с бригадой
    brigade: Mapped["Brigade | None"] = relationship("Brigade", back_populates="workers")
