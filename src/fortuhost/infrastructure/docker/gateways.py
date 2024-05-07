import datetime

from docker import DockerClient
from docker.models.containers import Container
from docker.types.daemon import CancellableStream

from fortuhost.domain.dto.instance import IdHex, InstanceDTO
from fortuhost.domain.dto.project import ProjectDTO
from fortuhost.domain.dto.user.user import UserDTO


class InstanceClientGateway:
    def __init__(self, client: DockerClient) -> None:
        self._client = client

    def get_instance(self, instance_id: IdHex) -> InstanceDTO:
        container: Container = self._client.containers.get(container_id=instance_id)
        return InstanceDTO(
            id=container.id,
            status=container.status
        )

    async def get_instance_project(self, instance_id: IdHex) -> ProjectDTO:
        raise NotImplementedError  # TODO реализовать

    async def get_instance_owner(self, instance_id: IdHex) -> UserDTO:
        raise NotImplementedError  # TODO реализовать

    def filter_instances(
            self,
            is_all: bool = True,
            filters: dict = None
    ) -> list[InstanceDTO]:
        """
         filters (dict): Filters to be processed on the image list.
                Available filters:

                - `exited` (int): Only containers with specified exit code
                - `status` (str): One of ``restarting``, ``running``,
                    ``paused``, ``exited``
                - `label` (str|list): format either ``"key"``, ``"key=value"``
                    or a list of such.
                - `id` (str): The id of the container.
                - `name` (str): The name of the container.
                - `ancestor` (str): Filter by container ancestor. Format of
                    ``<image-name>[:tag]``, ``<image-id>``, or
                    ``<image@digest>``.
                - `before` (str): Only containers created before a particular
                    container. Give the container name or id.
                - `since` (str): Only containers created after a particular
                    container. Give container name or id.
        """
        containers = self._client.containers.list(
            all=is_all,
            filters=filters
        )
        return containers


class DockerContainerGateway:
    """
        Class for control docker container
    """

    def __init__(self, client: DockerClient) -> None:
        self._client = client

    timeout = 5

    def start(self, instance_id: IdHex) -> None:
        """
            Start a docker container
            @param instance_id: container id. See 'docker ps' for get id
            @return: None
        """
        container: Container = self._client.containers.get(instance_id)
        container.start()

    def stop(self, instance_id: IdHex) -> None:
        """
            Stop a docker container
            @param instance_id: container id. See 'docker ps' for get id
            @return: None
        """
        container: Container = self._client.containers.get(instance_id)
        container.stop(timeout=self.timeout)
        container.wait()

    def restart(self, instance_id: IdHex) -> None:
        """
            Restart a docker container
            @param instance_id: container id. See 'docker ps' for get id
            @return: None
        """
        container: Container = self._client.containers.get(instance_id)
        container.restart(timeout=self.timeout)

    def delete(self, instance_id: IdHex) -> None:
        """
            Delete a docker container
            @param instance_id: container id. See 'docker ps' for get id
            @return: None
        """
        container = self._client.containers.get(instance_id)
        container.stop(timeout=self.timeout)
        container.remove()

    def get_logs_stream(self, instance_id: IdHex) -> CancellableStream:
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

    def get_status(self, instance_id: IdHex) -> str:
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
