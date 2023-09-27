from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/r",
)

@router.get("/")
async def react_root():
    return {"hello": "world"}