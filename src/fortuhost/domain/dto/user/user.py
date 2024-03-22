from dataclasses import dataclass
from uuid import UUID


@dataclass
class UserDTO:
    user_id: UUID
    email: str
    hashed_password: str
    is_active: bool
