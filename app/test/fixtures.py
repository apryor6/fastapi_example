import pytest

from app import create_app
from app.db import Base
from fastapi.testclient import TestClient


@pytest.fixture
def app():
    return create_app("test")


@pytest.fixture
def client(app):
    client = TestClient(app)
    return client


@pytest.fixture
def session(app):
    from app.db import get_db

    session = next(get_db())
    Base.metadata.drop_all()
    Base.metadata.create_all()
    yield session
    Base.metadata.drop_all()
    session.commit()
