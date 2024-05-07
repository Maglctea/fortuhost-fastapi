from fortuhost.domain.dto.base_type import IdHex
from fortuhost.domain.dto.instance import InstanceDTO, InstanceTaskDTO, InstanceConfigDTO
from fortuhost.domain.dto.project import ProjectDTO
from fortuhost.domain.dto.user.user import UserDTO


class InstanceClient:
    async def get_instance_project(self, instance_id: IdHex) -> ProjectDTO:
        raise NotImplementedError

    async def get_instance(self, instance_id: IdHex) -> InstanceDTO:
        raise NotImplementedError

    async def get_instance_owner(self, instance_id: IdHex) -> UserDTO:
        raise NotImplementedError

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
        raise NotImplementedError


class InstanceGateway:
    async def update_status(self, instance_id: IdHex, new_status: str) -> None:
        raise NotImplementedError


class InstanceControlGateway:
    def start(self, instance_id: IdHex) -> None:
        raise NotImplementedError

    def stop(self, instance_id: IdHex) -> None:
        raise NotImplementedError

    def restart(self, instance_id: IdHex) -> None:
        raise NotImplementedError

    def delete(self, instance_id: IdHex) -> None:
        raise NotImplementedError

    def get_status(self, container_id: IdHex) -> str:
        raise NotImplementedError

    def create(
            self,
            id_project: IdHex,
            config: InstanceConfigDTO
    ) -> InstanceDTO:
        raise NotImplementedError


class InstanceTaskGateway:
    async def get_tasks(self, count: int = None) -> list[InstanceTaskDTO]:
        raise NotImplementedError

    async def success_complete_task(self, task_id: IdHex) -> None:
        raise NotImplementedError

    async def failed_complete_task(self, task_id: IdHex) -> None:
        raise NotImplementedError
