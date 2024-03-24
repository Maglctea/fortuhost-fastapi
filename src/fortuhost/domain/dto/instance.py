from dataclasses import dataclass
from enum import Enum
from typing import NewType
from uuid import UUID

InstanceId = NewType("InstanceId", str)


class ActionTypeEnum(Enum):
    START = 'START'
    STOP = 'STOP'
    RESTART = 'RESTART'

    def __str__(self):
        return self.value
