from fortuhost.domain.dto.instance import InstanceId


class IInstanceControlGateway:
    def start(self, instance_id: InstanceId) -> None:
        raise NotImplementedError

    def stop(self, instance_id: InstanceId) -> None:
        raise NotImplementedError

    def restart(self, instance_id: InstanceId) -> None:
        raise NotImplementedError

    def delete(self, instance_id: InstanceId) -> None:
        raise NotImplementedError

    def get_status(self, container_id: InstanceId) -> str:
        raise NotImplementedError
