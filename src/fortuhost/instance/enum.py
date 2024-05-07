from enum import Enum


class ActionTypeEnum(Enum):
    START = 'START'
    STOP = 'STOP'
    RESTART = 'RESTART'
    DELETE = 'DELETE'

    def __str__(self):
        return self.value


class InstanceStatusEnum(Enum):
    RESTARTING = 'restarting'
    RUNNING = 'running'
    PAUSED = 'paused'
    EXITED = 'exited'

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
