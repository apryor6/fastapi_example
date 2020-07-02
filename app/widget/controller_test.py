from typing import List
from unittest.mock import patch

import pytest

from app.test.fixtures import client, app  # noqa
from .service import WidgetService
from .schema import WidgetSchema
from .model import Widget
from . import BASE_ROUTE


def make_widget(
    id: int = 123, name: str = "Test widget", purpose: str = "Test purpose"
) -> WidgetSchema:
    return WidgetSchema(widget_id=id, name=name, purpose=purpose)


async def fake_get_widgets(session) -> List[WidgetSchema]:
    return [
        make_widget(123, name="Test Widget 1"),
        make_widget(456, name="Test Widget 2"),
    ]


@patch.object(WidgetService, "get_all", fake_get_widgets)
def test_get_widget(client):  # noqa
    results = [WidgetSchema(**i) for i in client.get(f"/api/{BASE_ROUTE}").json()]
    print(results)
    expected: List[WidgetSchema] = [
        make_widget(123, name="Test Widget 1"),
        make_widget(456, name="Test Widget 2"),
    ]

    for r in results:
        assert r in expected

