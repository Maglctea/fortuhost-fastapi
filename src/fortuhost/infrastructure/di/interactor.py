from dishka import Provider, provide, Scope

from fortuhost.applications.user.interactors.auth import BaseLoginInteractor
from fortuhost.applications.instance.interactors import InstanceActionInteractor


class InteractorProvider(Provider):
    scope = Scope.REQUEST

    base_login = provide(BaseLoginInteractor)
    instance_action = provide(InstanceActionInteractor)

