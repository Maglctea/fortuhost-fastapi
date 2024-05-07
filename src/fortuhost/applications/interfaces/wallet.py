from fortuhost.domain.dto.instance import IdHex


class WalletGateway:
    async def pay_subscription(self, project_id: IdHex) -> None:
        raise NotImplementedError
