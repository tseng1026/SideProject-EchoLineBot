from typing import Any

from fastapi import APIRouter, HTTPException, Request
from linebot.exceptions import InvalidSignatureError

from app.dispatcher.v1.line import webhook_handler as handler

router = APIRouter()


@router.post("/callback")
async def handle_callback(request: Request) -> Any:
    signature = request.headers["X-Line-Signature"]
    body = await request.body()

    try:
        handler.handle(body.decode(), signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Missing Parameters")
    return "OK"
