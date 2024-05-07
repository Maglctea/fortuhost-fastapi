from fortuhost.domain.dto.instance import IdHex, InstanceTaskDTO


class InstanceNotificationGateway:
    def send_crash_report(self, recipient_id: IdHex, instance_id: IdHex) -> None:
        raise NotImplementedError

    def send_task_error_report(self, task: InstanceTaskDTO, reason: str) -> None:
        raise NotImplementedError
