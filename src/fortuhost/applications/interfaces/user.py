from fortuhost.domain.dto.instance import IdHex
from fortuhost.domain.dto.user.user import UserDTO


class IUserGateway:
    async def create_user(self, user: UserDTO) -> None:
        raise NotImplementedError

    async def get_user_by_id(self, user_id: int) -> UserDTO | None:
        raise NotImplementedError

    async def get_user_by_login(self, login: str) -> UserDTO | None:
        raise NotImplementedError