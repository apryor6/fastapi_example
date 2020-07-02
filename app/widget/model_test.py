from pytest import fixture
from app.test.fixtures import app, session  # noqa
from app.db import Session
from .model import Widget
from .schema import WidgetSchema


@fixture
def widget() -> WidgetSchema:
    widget = WidgetSchema(widget_id=1, name="Test widget", purpose="Test purpose")
    return Widget(**widget.dict())


def test_Widget_create(widget: WidgetSchema):
    assert widget


def test_Widget_retrieve(widget: Widget, session: Session):  # noqa
    session.add(widget)
    session.commit()
    s = session.query(Widget).first()
    assert s.__dict__ == widget.__dict__
