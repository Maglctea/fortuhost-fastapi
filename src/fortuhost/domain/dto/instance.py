from enum import Enum
from typing import NewType

InstanceId = NewType("InstanceId", str)


class ActionTypeEnum(Enum):
    START = 'START'
    STOP = 'STOP'
    RESTART = 'RESTART'

    def __str__(self):
        return self.value
