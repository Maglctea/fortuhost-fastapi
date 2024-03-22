from dataclasses import dataclass


@dataclass
class AdminConfig:
    host: str
    port: int
    debug: bool
    secret_key: str
