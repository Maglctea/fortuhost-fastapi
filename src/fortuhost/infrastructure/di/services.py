from dishka import Provider, provide, Scope

from fortuhost.infrastructure.auth.access import JWTGetUserService


class ServiceProvider(Provider):
    scope = Scope.REQUEST

    access = provide(JWTGetUserService)
