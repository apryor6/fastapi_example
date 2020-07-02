import os
from typing import List, Type

from pydantic import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    CONFIG_NAME: str = "base"
    USE_MOCK_EQUIVALENCY: bool = False
    DEBUG: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class DevelopmentConfig(Settings):
    CONFIG_NAME: str = "dev"
    SECRET_KEY: str = os.getenv(
        "DEV_SECRET_KEY", "You can't see California without Marlon Widgeto's eyes"
    )
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///{0}/app-dev.db".format(basedir)


class TestingConfig(Settings):
    CONFIG_NAME: str = "test"
    SECRET_KEY: str = os.getenv("TEST_SECRET_KEY", "Thanos did nothing wrong")
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///{0}/app-test.db".format(basedir)


class ProductionConfig(Settings):
    CONFIG_NAME: str = "prod"
    SECRET_KEY: str = os.getenv("PROD_SECRET_KEY", "I'm Ron Burgundy?")
    DEBUG: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///{0}/app-prod.db".format(basedir)


def get_config():
    return config_by_name[os.environ["ENV"]]


EXPORT_CONFIGS: List[Type[Settings]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]
config_by_name = {cfg().CONFIG_NAME: cfg() for cfg in EXPORT_CONFIGS}
