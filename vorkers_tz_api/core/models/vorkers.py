from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class Vorkers(Base):
    __tablename__ = "vorkers"

    full_name: Mapped[str] = mapped_column(String, nullable=False)
    number_brigade: Mapped[int] = mapped_column(Integer, nullable=False)
    salary: Mapped[float] = mapped_column(Float, nullable=False)
    specialization: Mapped[str] = mapped_column(String, nullable=False)
