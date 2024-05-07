from dishka import Provider, Scope, provide

from fortuhost.applications.interfaces.user import IUserGateway
from fortuhost.applications.interfaces.instance import InstanceControlGateway, InstanceClient, InstanceTaskGateway
from fortuhost.infrastructure.db.gateways.user.user import UserGateway
from fortuhost.infrastructure.docker.gateways import DockerContainerGateway


class GatewaysProvider(Provider):
    scope = Scope.REQUEST

    user_gateway = provide(
        source=UserGateway,
        provides=IUserGateway
    )

    instance_client = provide(
        source=DockerContainerGateway,
        provides=InstanceClient
    )

    instance_gateway = provide(
        source=DockerContainerGateway,
        provides=InstanceControlGateway
    )

    instance_task_gateway = provide(
        source=DockerContainerGateway,
        provides=InstanceTaskGateway
    )


