from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/ping/", response_class=JSONResponse)
async def ping():
    return JSONResponse(
        status_code=200,
        content={"message": "pong"}
    )
