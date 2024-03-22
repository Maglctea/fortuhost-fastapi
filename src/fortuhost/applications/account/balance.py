from fortuhost.applications.interfaces.account import IUserGateway
from fortuhost.applications.interfaces.uow import IUoW
from fortuhost.domain.dto.user.user import UserDTO
from fortuhost.domain.services.security import hash_secret


class CreateAccountInteractor:
    def __init__(
            self,
            user_gateway: IUserGateway,
            unit_of_work: IUoW,
    ) -> None:
        self.user_gateway = user_gateway
        self.unit_of_work = unit_of_work

    async def __call__(
            self,
            user: UserDTO
    ) -> None:
        user.hashed_password = hash_secret(user.hashed_password)
        await self.user_gateway.create_user(user)
        await self.unit_of_work.commit()
