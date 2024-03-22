
from dataclasses import dataclass


@dataclass
class CeleryConfig:
    broker_url: str
    result_backend_url: str
