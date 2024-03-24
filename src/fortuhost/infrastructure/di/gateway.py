from dishka import Provider, Scope, provide

from fortuhost.applications.interfaces.account import IUserGateway
from fortuhost.applications.interfaces.instance import IInstanceControlGateway
from fortuhost.infrastructure.db.gateways.user.user import UserGateway
from fortuhost.infrastructure.docker.gateways import DockerContainerGateway


class GatewaysProvider(Provider):
    scope = Scope.REQUEST

    user_gateway = provide(
        source=UserGateway,
        provides=IUserGateway
    )

    instance_gateway = provide(
        source=DockerContainerGateway,
        provides=IInstanceControlGateway
    )
