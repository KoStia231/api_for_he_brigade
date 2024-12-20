from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.base_views import (
    get_all_object, get_object_by_id,
    create_object, update_object,
    delete_object
)
from core.database import db_helper
from core.models import Worker
from core.schemas import (
    WorkerCreate,
    WorkerUpdate,
    WorkerResponse
)

router = APIRouter()


@router.get("/", response_model=list[WorkerResponse])
async def get_workers_view(
        session: AsyncSession = Depends(db_helper.session_getter),
):
    workers = await get_all_object(Worker, session=session)
    return workers


@router.get("/{worker_id}", response_model=WorkerResponse)
async def get_worker_view(
        worker_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    worker = await get_object_by_id(Worker, session=session, object_id=worker_id)
    return worker


@router.post("/", response_model=WorkerResponse)
async def create_worker_view(
        worker: WorkerCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    new_worker = await create_object(Worker, session=session, data=worker)
    return new_worker


@router.put("/{worker_id}", response_model=WorkerResponse)
async def update_worker_view(
        worker_id: int, worker: WorkerUpdate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    updated_worker = await update_object(Worker, session=session, object_id=worker_id, data=worker)
    return updated_worker


@router.delete("/{worker_id}")
async def delete_author_view(
        worker_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    await delete_object(Worker, session=session, object_id=worker_id)
    return {"message": "Workers deleted successfully"}
