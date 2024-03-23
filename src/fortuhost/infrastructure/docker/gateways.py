import datetime

from docker import DockerClient
from docker.models.containers import Container
from docker.types.daemon import CancellableStream

from fortuhost.domain.dto.instance import InstanceId


class DockerContainerGateway:
    """
        Class for control docker container
    """
    def __init__(self, client: DockerClient) -> None:
        self._client = client

    timeout = 5

    def start(self, instance_id: InstanceId) -> None:
        """
            Start a docker container
            @param instance_id: container id. See 'docker ps' for get id
            @return: None
        """
        container: Container = self._client.containers.get(instance_id)
        container.start()

    def stop(self, instance_id: InstanceId) -> None:
        """
            Stop a docker container
            @param instance_id: container id. See 'docker ps' for get id
            @return: None
        """
        container: Container = self._client.containers.get(instance_id)
        container.stop(timeout=self.timeout)
        container.wait()

    def restart(self, instance_id: InstanceId) -> None:
        """
            Restart a docker container
            @param instance_id: container id. See 'docker ps' for get id
            @return: None
        """
        container: Container = self._client.containers.get(instance_id)
        container.restart(timeout=self.timeout)

    def delete(self, instance_id: InstanceId) -> None:
        """
            Delete a docker container
            @param instance_id: container id. See 'docker ps' for get id
            @return: None
        """
        container = self._client.containers.get(instance_id)
        container.stop(timeout=self.timeout)
        container.remove()

    def get_logs_stream(self, instance_id: InstanceId) -> CancellableStream:
        """
            Get iterator for viewing logs
            @param instance_id: container id. See 'docker ps' for get id
            @return: returns a sync iterator for viewing logs
        """
        container = self._client.containers.get(instance_id)
        return container.logs(
            stream=True,
            timestamps=True,
            since=datetime.datetime.now() - datetime.timedelta(hours=1),
            tail=300
        )

    def get_status(self, instance_id: InstanceId) -> str:
        """
            Get the status of a docker container
            @param instance_id: container id. See 'docker ps' for get id
            @return: status of docker container
        """
        container = self._client.containers.get(instance_id)
        return container.status

    def create(
            self,
            name: str,
            registry_url: str,
            image_name: str,
            command: str,
            env: dict,
            network_id: str
    ) -> Container:
        """
            Create a new container and mount it to the network
            @param name: name of the container. Valid name mask: [a-zA-Z0-9.-]+
            @param registry_url: address of the registry
            @param image_name: name of the image in the registry
            @param command: the command that is triggered every time you start.
            @param env: dictionary of local variables
            @param network_id: network ID. See 'docker network ls'
            @return: None
        """
        container = self._client.containers.run(
            name=name,
            image=f"{registry_url}/{image_name}",
            environment=env,
            command=command,
            detach=True,
            network=network_id,
            restart_policy={'Name': 'on-failure'},
            mem_limit='1g'
        )
        return container
