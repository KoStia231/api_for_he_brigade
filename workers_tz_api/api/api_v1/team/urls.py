from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.base_views import (
    get_all_object, get_object_by_id,
    create_object, update_object,
    delete_object
)
from core.database import db_helper
from core.models import Brigade
from core.schemas import (
    BrigadeCreate,
    BrigadeUpdate,
    BrigadesResponse,
    BrigadeResponse
)

router = APIRouter()


@router.get("/", response_model=list[BrigadesResponse])
async def get_brigades_view(
        session: AsyncSession = Depends(db_helper.session_getter),
):
    brigades = await get_all_object(Brigade, session=session)
    return brigades


@router.get("/{brigade_id}/WorkerList", response_model=BrigadeResponse)
async def get_brigade_view(
        brigade_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    brigade = await get_object_by_id(Brigade, session=session, object_id=brigade_id)
    await session.refresh(brigade, ["workers"])
    return brigade


@router.post("/", response_model=BrigadesResponse)
async def create_brigade_view(
        brigade: BrigadeCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    new_brigade = await create_object(Brigade, session=session, data=brigade)
    return new_brigade


@router.put("/{brigade_id}", response_model=BrigadesResponse)
async def update_brigade_view(
        brigade_id: int, brigade: BrigadeUpdate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    updated_brigade = await update_object(Brigade, session=session, object_id=brigade_id, data=brigade)
    return updated_brigade


@router.delete("/{brigade_id}")
async def delete_brigade_view(
        brigade_id: int,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    await delete_object(Brigade, session=session, object_id=brigade_id)
    return {"message": "Brigade deleted successfully"}
