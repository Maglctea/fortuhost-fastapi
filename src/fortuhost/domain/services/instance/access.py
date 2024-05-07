from fortuhost.applications.interfaces.instance import InstanceClient
from fortuhost.applications.interfaces.permission import PermissionGateway
from fortuhost.applications.interfaces.project import ProjectGateway
from fortuhost.domain.dto.instance import IdHex, InstancePermissionEnum


class InstanceControlAccessService:
    def __init__(
            self,
            instance_client_gateway: InstanceClient,
            project_gateway: ProjectGateway,
            permission_gateway: PermissionGateway,
    ):
        self.instance_client_gateway = instance_client_gateway
        self.project_gateway = project_gateway
        self.permission_gateway = permission_gateway

    async def is_can_start(
            self,
            user_id: IdHex,
            instance_id: IdHex,
            action: InstancePermissionEnum
    ) -> bool:
        project = await self.instance_client_gateway.get_instance_project(instance_id)

        if user_id == project.owner.user_id:
            return True

        permissions = await self.permission_gateway.get_user_permissions(
            user_id=user_id,
            project_id=project.id
        )
        if action in permissions:
            return True

        return False

    async def is_can_perform_action(
            self,
            user_id: IdHex,
            instance_id: IdHex,
            action: InstancePermissionEnum
    ) -> bool:
        project = await self.instance_client_gateway.get_instance_project(instance_id)

        if user_id == project.owner.user_id:
            return True

        permissions = await self.permission_gateway.get_user_permissions(
            user_id=user_id,
            project_id=project.id
        )
        if action in permissions:
            return True

        return False