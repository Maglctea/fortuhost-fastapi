from typing import Union, Annotated

from dishka.integrations.fastapi import inject, FromDishka
from fastapi import Header, Response, status, HTTPException, APIRouter
from fastapi.responses import JSONResponse

from fortuhost.applications.user.interactors.auth import BaseLoginInteractor
from fortuhost.domain.exceptions.user import UserNotFoundException

auth_router = APIRouter(
    tags=["Auth"],
    prefix='/auth'
)


@auth_router.post(
    path='/login',
    description='Gets a token for interacting with the site API',
    response_description='JWT token for interacting with the site API',
    response_model=None,
)
@inject
async def login(
        base_login_interactor: Annotated[BaseLoginInteractor, FromDishka()],
        login: str = Header(
            description='email or phone number used during services registration',
            example='ivan@gmail.com'
        ),
        password: str = Header(
            description='password used during services registration',
            example='VeryHardPassword_777'
        )
) -> Union[Response, HTTPException]:
    try:
        token = await base_login_interactor(
            login=login,
            password=password
        )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "access_token": token,
                "token_type": "bearer"
            }
        )
    except UserNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid authorization data',
            headers={"WWW-Authenticate": "Bearer"}
        )
