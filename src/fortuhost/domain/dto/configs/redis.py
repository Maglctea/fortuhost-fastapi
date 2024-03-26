from dataclasses import dataclass


@dataclass
class RedisConfig:
    host: str
    port: int
    password: str | None = None
