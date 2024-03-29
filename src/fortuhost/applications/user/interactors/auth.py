from fortuhost.applications.interfaces.account import IUserGateway
from fortuhost.applications.interfaces.uow import IUoW
from fortuhost.domain.exceptions.user import UserNotFoundException
from fortuhost.domain.dto.configs.auth import AuthConfig
from fortuhost.infrastructure.security import hash_secret, generate_jwt_token


class BaseLoginInteractor:
    def __init__(
            self,
            user_gateway: IUserGateway,
            unit_of_work: IUoW,
            auth_config: AuthConfig
    ) -> None:
        self.user_gateway = user_gateway
        self.unit_of_work = unit_of_work
        self.auth_config = auth_config

    async def __call__(
            self,
            login: str,
            password: str
    ) -> str:
        user = await self.user_gateway.get_user_by_login(login)

        if user is not None:
            if user.hashed_password == hash_secret(password):
                token = generate_jwt_token(
                    user_id=user.user_id,
                    expires_delta_minutes=self.auth_config.token_expire_minutes,
                    algorithm=self.auth_config.algorithm,
                    secret_key=self.auth_config.secret_key
                )
                return token

        raise UserNotFoundException('The user with such private data was not found')
