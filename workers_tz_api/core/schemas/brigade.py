from typing import Optional, List
from pydantic import BaseModel

from .workers import (
    WorkerCreate,
    WorkerResponse,
)


class BrigadeBase(BaseModel):
    name: str


class BrigadeCreate(BrigadeBase):
    workers: Optional[List[WorkerCreate]] = None


class BrigadeUpdate(BaseModel):
    name: Optional[str] = None
    workers: Optional[List[WorkerCreate]] = None


class BrigadeResponse(BaseModel):
    workers: List[WorkerResponse] = []


class BrigadesResponse(BrigadeBase):
    id: int

