from dishka import Provider, provide, Scope

from fortuhost.applications.account.interactors.auth import BaseLoginInteractor


class InteractorProvider(Provider):
    scope = Scope.REQUEST

    base_login = provide(BaseLoginInteractor)

