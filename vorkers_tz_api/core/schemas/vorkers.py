from typing import Optional

from pydantic import BaseModel


class VorkersBase(BaseModel):
    full_name: str
    number_brigade: int
    salary: float
    specialization: str


class VorkersCreate(VorkersBase):
    pass


class VorkersUpdate(BaseModel):
    full_name: Optional[str] = None
    number_brigade: Optional[int] = None
    salary: Optional[float] = None
    specialization: Optional[str] = None


class VorkersResponse(VorkersBase):
    id: int
