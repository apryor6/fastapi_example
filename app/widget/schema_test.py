from pytest import fixture

from .model import Widget
from .schema import WidgetSchema


def test_WidgetSchema_works():
    widget: WidgetSchema = WidgetSchema(
        **{"widget_id": 123, "name": "Test widget", "purpose": "Test purpose"}
    )

    assert widget.widget_id == 123
    assert widget.name == "Test widget"
    assert widget.purpose == "Test purpose"
