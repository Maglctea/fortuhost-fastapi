from dishka import Provider, provide, Scope

from fortuhost.applications.user.services.access import JWTGetUserService


class ServiceProvider(Provider):
    scope = Scope.REQUEST

    access = provide(JWTGetUserService)
