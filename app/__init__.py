import os

from fastapi import FastAPI

from .config import get_config
from .routes import register_routes


def create_app(config="dev"):
    settings = get_config(config=config)

    app = FastAPI(title="Fasterific API")

    register_routes(app)

    @app.get("/")
    def index():
        return settings.CONFIG_NAME

    @app.get("/health")
    def health():
        return {"status": "healthy"}

    return app
