from fortuhost.applications.interfaces.instance import IInstanceControlGateway
from fortuhost.domain.dto.instance import InstanceId


class ContainerDeleteInteractor:
    def __init__(
            self,
            container_gateway: IInstanceControlGateway
    ) -> None:
        self.container_gateway = container_gateway

    async def __call__(
            self,
            container_id: InstanceId,
    ) -> None:
        self.container_gateway.delete(container_id)


class ContainerRestartInteractor:
    def __init__(
            self,
            container_gateway: IInstanceControlGateway
    ) -> None:
        self.container_gateway = container_gateway

    async def __call__(
            self,
            container_id: InstanceId,
    ) -> None:
        self.container_gateway.restart(container_id)


class ContainerStartInteractor:
    def __init__(
            self,
            container_gateway: IInstanceControlGateway
    ) -> None:
        self.container_gateway = container_gateway

    async def __call__(
            self,
            container_id: InstanceId,
    ) -> None:
        self.container_gateway.start(container_id)


class ContainerStopInteractor:
    def __init__(
            self,
            container_gateway: IInstanceControlGateway
    ) -> None:
        self.container_gateway = container_gateway

    async def __call__(
            self,
            container_id: InstanceId,
    ) -> None:
        self.container_gateway.stop(container_id)
