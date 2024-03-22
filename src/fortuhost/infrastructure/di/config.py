from dishka import Provider, Scope, provide

from fortuhost.domain.dto.configs.api import APIConfig
from fortuhost.domain.dto.configs.auth import AuthConfig
from fortuhost.domain.dto.configs.db import DBConfig
from fortuhost.infrastructure.config_loader import load_config


class BaseConfigProvider(Provider):
    scope = Scope.APP


class APIConfigProvider(BaseConfigProvider):

    @provide
    def get_api_config(self) -> APIConfig:
        return load_config(
            config_type=APIConfig,
            config_scope='api'
        )


class DBConfigProvider(BaseConfigProvider):

    @provide
    def get_db_config(self) -> DBConfig:
        return load_config(
            config_type=DBConfig,
            config_scope='db'
        )


class AuthConfigProvider(BaseConfigProvider):

    @provide
    def get_auth_config(self) -> AuthConfig:
        return load_config(
            config_type=AuthConfig,
            config_scope='auth'
        )
