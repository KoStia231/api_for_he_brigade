from typing import Optional

from pydantic import BaseModel


class WorkerBase(BaseModel):
    full_name: str
    salary: float
    specialization: str
    brigade_id: Optional[int] = None


class WorkerCreate(WorkerBase):
    pass


class WorkerUpdate(BaseModel):
    full_name: Optional[str] = None
    salary: Optional[float] = None
    specialization: Optional[str] = None
    brigade_id: Optional[int] = None


class WorkerResponse(WorkerBase):
    id: int
