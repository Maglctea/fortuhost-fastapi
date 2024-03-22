from dataclasses import dataclass


@dataclass
class AuthConfig:
    secret_key: str
    token_expire_minutes: int
    algorithm: str = "HS256"

