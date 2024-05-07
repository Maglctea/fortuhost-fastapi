from fortuhost.domain.dto.instance import IdHex


class PermissionGateway:
    async def get_user_permissions(self, project_id: IdHex, user_id: IdHex) -> list[str]:
        raise NotImplementedError
