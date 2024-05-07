from typing import NewType

InstanceId = NewType("InstanceId", str)


class InstanceDTO:
    id: InstanceId
    status: str

