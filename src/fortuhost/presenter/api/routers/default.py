from fastapi import APIRouter
from fastapi import status
from fastapi.responses import RedirectResponse

default_router = APIRouter(
    prefix="",
    tags=["default"],
    include_in_schema=False,
)


@default_router.get("/")
async def default_redirect() -> RedirectResponse:
    return RedirectResponse(
        url="/docs",
        status_code=status.HTTP_302_FOUND,
    )
