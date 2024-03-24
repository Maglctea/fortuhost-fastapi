import os
import tomllib
from typing import TypeVar

from adaptix import Retort

T = TypeVar("T")


def read_toml(path: str) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)


def load_config(
        config_type: type[T],
        config_scope: str | None = None,
) -> T:

    path = os.getenv("FORTUHOST_CONFIG_PATH")

    if path is None:
        raise Exception("FORTUHOST_CONFIG_PATH is not set in environment variables")

    data = read_toml(f"{path}/config.toml")

    if config_scope is not None:
        data = data[config_scope]

    dcf = Retort()
    config = dcf.load(data, config_type)
    return config
