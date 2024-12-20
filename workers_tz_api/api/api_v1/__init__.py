from fastapi import APIRouter
from .worker.urls import router as worker_router
from .team.urls import router as team_router
from core import se

api_v1_router = APIRouter()

api_v1_router.include_router(worker_router, prefix=se.api.v1.worker, tags=["worker"])
api_v1_router.include_router(team_router, prefix=se.api.v1.team, tags=["team"])
