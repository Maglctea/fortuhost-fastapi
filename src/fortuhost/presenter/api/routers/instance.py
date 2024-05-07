from typing import Union, Annotated

from dishka.integrations.fastapi import inject, FromDishka
from fastapi import Response, status, HTTPException, APIRouter, Body, Header
from fastapi.responses import JSONResponse

from fortuhost.applications.instance.interactors import InstanceActionInteractor
from fortuhost.domain.dto.instance import IdHex
from fortuhost.domain.exceptions.user import UserNotFoundError, AccessDeniedError

instance_router = APIRouter(
    tags=["Auth"],
    prefix='/instance'
)


@instance_router.post(
    path='/action',
    description='Instance action (start/stop/restart)',
    response_description='Base response (detail: ok)',
    response_model=None,
)
@inject
async def instance_action(
        instance_action_interactor: Annotated[InstanceActionInteractor, FromDishka()],
        token: str = Header(
            description='Access token',
            example='df4gdfg3ghj42dfg3r'
        ),
        instance_id: IdHex = Body(
            example='sxzf1sfadf1'
        ),
        action: str = Body(
            description='Instance action (start/stop/restart)',
            example='start'
        )
) -> Union[Response, HTTPException]:
    try:
        await instance_action_interactor(
            token=token,
            instance_id=instance_id,
            action=action,
        )
    except (UserNotFoundError, AccessDeniedError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid authorization data',
            headers={"WWW-Authenticate": "Bearer"}
        )

    return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"detail": "ok"}
        )
