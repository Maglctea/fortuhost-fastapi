from fortuhost.domain.dto.instance import IdHex


class ProjectGateway:
    async def is_paid(self, project_id: IdHex) -> bool:
        raise NotImplementedError
