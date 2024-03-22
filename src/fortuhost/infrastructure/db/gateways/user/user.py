from adaptix import Retort
from sqlalchemy import select

from fortuhost.domain.dto.user.user import UserDTO
from fortuhost.infrastructure.db.gateways.base import SQLAlchemyGateway
from fortuhost.infrastructure.db.models.user import User


class UserGateway(SQLAlchemyGateway):
    async def create_user(self, user: UserDTO) -> None:
        account = User(**user.dict())  # TODO переписать с pydantic на dataclass
        self._session.add(account)

    async def get_user_by_id(self, user_id: int) -> UserDTO | None:
        user = await self._session.get(User, user_id)

        if user is None:
            return None

        dcf = Retort()
        user_data = dcf.load(user, UserDTO)
        return user_data

    async def get_user_by_login(self, login: str) -> UserDTO | None:
        user = await self._session.scalar(
            select(User)
            .where(User.email == login)
        )

        if user is None:
            return None

        dcf = Retort()
        user_data = dcf.load(user, UserDTO)
        return user_data
