from pytest import fixture

from .model import Fizz
from .schema import FizzSchema


def test_FizzSchema_works():
    fizz: FizzSchema = FizzSchema(
        **{"fizz_id": 123, "name": "Test fizz", "purpose": "Test purpose"}
    )

    assert fizz.fizz_id == 123
    assert fizz.name == "Test fizz"
    assert fizz.purpose == "Test purpose"
