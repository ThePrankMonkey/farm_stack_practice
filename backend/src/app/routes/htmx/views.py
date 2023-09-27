from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/h",
)

@router.get("/")
async def htmx_root():
    html_content = """
    <div>
    Hello World!
    </div>
    """
    return HTMLResponse(content=html_content, status_code=200)