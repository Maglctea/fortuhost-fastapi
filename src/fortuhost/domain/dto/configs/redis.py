from dataclasses import dataclass


@dataclass
class RedisConfig:
    host: str = "localhost"
    port: int = 6379
    password: str | None = None
