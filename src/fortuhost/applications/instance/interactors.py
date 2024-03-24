from fortuhost.applications.user.services.access import JWTGetUserService
from fortuhost.applications.interfaces.instance import IInstanceControlGateway
from fortuhost.domain.dto.instance import InstanceId, ActionTypeEnum
from fortuhost.domain.services.security import is_access


class InstanceActionInteractor:
    def __init__(
            self,
            instance_gateway: IInstanceControlGateway,
            jwt_get_user_service: JWTGetUserService
    ) -> None:
        self.instance_gateway = instance_gateway
        self.jwt_get_user_service = jwt_get_user_service

    async def __call__(
            self,
            token: str,
            instance_id: InstanceId,
            action: ActionTypeEnum | str
    ) -> None:
        user = await self.jwt_get_user_service(token)
        if is_access(..., ...):  # TODO: implement this method
            match action:
                case ActionTypeEnum.START:
                    self.instance_gateway.start(instance_id)
                case ActionTypeEnum.RESTART:
                    self.instance_gateway.restart(instance_id)
                case ActionTypeEnum.STOP:
                    self.instance_gateway.stop(instance_id)
