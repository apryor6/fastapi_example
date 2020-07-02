from app.test.fixtures import app, client  # noqa


def test_app_creates(app):  # noqa
    assert app


def test_app_healthy(app, client):  # noqa
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "healthy"}
