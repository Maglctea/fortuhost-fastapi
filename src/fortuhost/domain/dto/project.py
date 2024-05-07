from dataclasses import dataclass
from datetime import datetime

from fortuhost.domain.dto.base_type import IdHex
from fortuhost.domain.dto.user.user import UserDTO


@dataclass
class ProjectDTO:
    id: IdHex
    name: str
    owner: UserDTO
    is_active: bool
    next_payment_date: datetime
