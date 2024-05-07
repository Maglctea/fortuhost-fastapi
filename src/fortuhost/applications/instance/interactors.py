from fortuhost.infrastructure.auth.access import JWTGetUserService
from fortuhost.applications.interfaces.instance import InstanceControlGateway
from fortuhost.domain.dto.instance import IdHex, ActionTypeEnum
from fortuhost.infrastructure.auth.security import is_access


class InstanceActionInteractor:
    def __init__(
            self,
            instance_gateway: InstanceControlGateway,
            jwt_get_user_service: JWTGetUserService
    ) -> None:
        self.instance_gateway = instance_gateway
        self.jwt_get_user_service = jwt_get_user_service

    async def __call__(
            self,
            token: str,
            instance_id: IdHex,
            action: ActionTypeEnum | str
    ) -> None:
        user = await self.jwt_get_user_service(token)
        if is_access(user, ...):  # TODO: implement this method
            match action:
                case ActionTypeEnum.START:
                    self.instance_gateway.start(instance_id)
                case ActionTypeEnum.RESTART:
                    self.instance_gateway.restart(instance_id)
                case ActionTypeEnum.STOP:
                    self.instance_gateway.stop(instance_id)
