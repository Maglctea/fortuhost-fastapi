from fastapi import FastAPI

from fortuhost.presenter.api.routers.auth import auth_router
from fortuhost.presenter.api.routers.instance import instance_router
from fortuhost.presenter.api.routers.default import default_router


def setup_controllers(app: FastAPI) -> None:
    app.include_router(default_router)
    app.include_router(instance_router)
    app.include_router(auth_router)
