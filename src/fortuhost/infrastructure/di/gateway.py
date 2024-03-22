from dishka import Provider, Scope, provide

from fortuhost.applications.interfaces.account import IUserGateway
from fortuhost.infrastructure.db.gateways.user.user import UserGateway


class GatewaysProvider(Provider):
    scope = Scope.REQUEST

    user_gateway = provide(
        source=UserGateway,
        provides=IUserGateway
    )
