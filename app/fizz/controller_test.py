from typing import List
from unittest.mock import patch

import pytest

from app.test.fixtures import client, app  # noqa
from .service import FizzService
from .schema import FizzSchema
from .model import Fizz
from . import BASE_ROUTE


def make_fizz(
    id: int = 123, name: str = "Test fizz", purpose: str = "Test purpose"
) -> FizzSchema:
    return FizzSchema(fizz_id=id, name=name, purpose=purpose)


async def fake_get_fizzs(session) -> List[FizzSchema]:
    return [
        make_fizz(123, name="Test Fizz 1"),
        make_fizz(456, name="Test Fizz 2"),
    ]


@patch.object(FizzService, "get_all", fake_get_fizzs)
def test_get_fizz(client):  # noqa
    results = [FizzSchema(**i) for i in client.get(f"/api/{BASE_ROUTE}").json()]
    print(results)
    expected: List[FizzSchema] = [
        make_fizz(123, name="Test Fizz 1"),
        make_fizz(456, name="Test Fizz 2"),
    ]

    for r in results:
        assert r in expected

