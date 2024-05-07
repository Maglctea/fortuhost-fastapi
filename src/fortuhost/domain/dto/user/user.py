from dataclasses import dataclass
from uuid import UUID

from fortuhost.domain.dto.base_type import IdHex


@dataclass
class UserDTO:
    user_id: IdHex
    email: str
    hashed_password: str
    is_active: bool
