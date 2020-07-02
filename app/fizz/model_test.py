from pytest import fixture
from app.test.fixtures import app, session  # noqa
from app.db import Session
from .model import Fizz
from .schema import FizzSchema


@fixture
def fizz() -> FizzSchema:
    fizz = FizzSchema(fizz_id=1, name="Test fizz", purpose="Test purpose")
    return Fizz(**fizz.dict())


def test_Fizz_create(fizz: FizzSchema):
    assert fizz


def test_Fizz_retrieve(fizz: Fizz, session: Session):  # noqa
    session.add(fizz)
    session.commit()
    s = session.query(Fizz).first()
    assert s.__dict__ == fizz.__dict__
