from dishka import Provider, Scope, provide
from docker import DockerClient


class InstanceProvider(Provider):
    scope = Scope.APP

    @provide
    def get_docker_client(self) -> DockerClient:
        return DockerClient()
