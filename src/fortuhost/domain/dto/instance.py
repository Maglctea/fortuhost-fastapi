from dataclasses import dataclass
from enum import Enum

from fortuhost.domain.dto.base_type import IdHex


class ActionTypeEnum(Enum):
    START = 'START'
    STOP = 'STOP'
    RESTART = 'RESTART'

    def __str__(self):
        return self.value


class InstanceStatusEnum(Enum):
    RESTARTING = 'restarting'
    RUNNING = 'running'
    PAUSED = 'paused'
    EXITED = 'exited'

    def __str__(self):
        return self.value


class InstancePermissionEnum(Enum):
    CAN_START = 'instance_can_start'
    CAN_STOP = 'instance_can_stop'
    CAN_RESTART = 'instance_can_restart'
    CAN_DELETE = 'instance_can_delete'
    CAN_CREATE = 'instance_can_create'

    def __str__(self):
        return self.value


class InstanceExitCodeEnum(Enum):
    OK = 0
    APP_ERROR = 1
    FAILED_START = 125

    def __int__(self):
        return self.value

    def __str__(self):
        return str(self.value)


@dataclass
class InstanceDTO:
    id: IdHex
    status: str


@dataclass
class InstanceTaskDTO:
    task_id: IdHex
    user_id: str
    instance_id: IdHex
    type: ActionTypeEnum | str


@dataclass
class InstanceConfigDTO:
    command: str
    image: str
    # TODO надо будет добавить поля
