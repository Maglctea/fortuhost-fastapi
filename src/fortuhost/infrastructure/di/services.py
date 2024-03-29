from dishka import Provider, provide, Scope

from fortuhost.infrastructure.access import JWTGetUserService


class ServiceProvider(Provider):
    scope = Scope.REQUEST

    access = provide(JWTGetUserService)
