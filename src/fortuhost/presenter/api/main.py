import logging

import uvicorn
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fortuhost.domain.dto.configs.api import APIConfig
from fortuhost.infrastructure.di.config import APIConfigProvider, DBConfigProvider, AuthConfigProvider
from fortuhost.infrastructure.di.db import DbProvider
from fortuhost.infrastructure.di.gateway import GatewaysProvider
from fortuhost.infrastructure.di.instance import InstanceProvider
from fortuhost.infrastructure.di.interactor import InteractorProvider
from fortuhost.infrastructure.di.services import ServiceProvider
from fortuhost.presenter.api.routers.main import setup_controllers

logger = logging.getLogger(__name__)


def init_api(
        debug: bool,
) -> FastAPI:
    logger.debug("Initialize API")
    app = FastAPI(
        debug=debug,
        title="User service",
        version="1.0.0",
        default_response_class=JSONResponse
    )
    setup_controllers(app)
    return app


async def run_api(
        app: FastAPI,
        api_config: APIConfig
) -> None:
    config = uvicorn.Config(
        app,
        host=api_config.host,
        port=api_config.port,
        reload=api_config.debug,
    )
    server = uvicorn.Server(config)
    logger.info("Running API")
    await server.serve()


async def main() -> None:
    container = make_async_container(
        *[
            APIConfigProvider(),
            DBConfigProvider(),
            AuthConfigProvider(),
            DbProvider(),
            InteractorProvider(),
            GatewaysProvider(),
            InstanceProvider(),
            ServiceProvider()
        ]
    )

    config = await container.get(APIConfig)
    app = init_api(config.debug)

    if config.debug:
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        logger.addHandler(console_handler)

    setup_dishka(container, app)

    await run_api(
        app=app,
        api_config=config
    )
