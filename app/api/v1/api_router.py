from fastapi import APIRouter

from app.api.v1.endpoints import linebot

api_router = APIRouter()
api_router.include_router(linebot.router, tags=["linebot"])
