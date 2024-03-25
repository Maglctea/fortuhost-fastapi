from starlette import status
from starlette.responses import JSONResponse


def simple_api_response(content: dict | None = None) -> JSONResponse:
    if content is None:
        content = {
            "detail": "OK"
        }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=content
    )
