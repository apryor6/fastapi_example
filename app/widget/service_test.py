from typing import List

import pytest

from app.test.fixtures import app, session  # noqa
from app.db import Session
from .model import Widget
from .service import WidgetService  # noqa
from .schema import WidgetSchema


@pytest.mark.asyncio
async def test_get_all(session: Session):  # noqa
    yin: WidgetSchema = WidgetSchema(widget_id=1, name="Yin", purpose="thing 1")
    yang: WidgetSchema = WidgetSchema(widget_id=2, name="Yang", purpose="thing 2")
    session.add(Widget(**yin.dict()))
    session.add(Widget(**yang.dict()))
    session.commit()

    results: List[WidgetSchema] = await WidgetService.get_all(session)

    assert len(results) == 2
    assert yin in results and yang in results


@pytest.mark.asyncio
async def test_update(session: Session):  # noqa
    yin: WidgetSchema = WidgetSchema(widget_id=1, name="Yin", purpose="thing 1")
    yin_orm = Widget(**yin.dict())
    session.add(yin_orm)
    updates: WidgetSchema = WidgetSchema(
        widget_id=1, name="New Widget name", purpose="thing 1"
    )

    await WidgetService.update(yin_orm, updates, session)
    result: WidgetSchema = session.query(Widget).get(yin.widget_id)
    assert result.name == "New Widget name"


@pytest.mark.asyncio
async def test_delete_by_id(session: Session):  # noqa
    yin: WidgetSchema = WidgetSchema(widget_id=1, name="Yin", purpose="thing 1")
    yang: WidgetSchema = WidgetSchema(widget_id=2, name="Yang", purpose="thing 2")

    yin_orm = Widget(**yin.dict())
    yang_orm = Widget(**yang.dict())

    session.add(yin_orm)
    session.add(yang_orm)
    session.commit()

    await WidgetService.delete_by_id(1, session)
    session.commit()

    results: List[Widget] = session.query(Widget).all()

    assert len(results) == 1
    assert yin_orm not in results and yang_orm in results


@pytest.mark.asyncio
async def test_create(session: Session):  # noqa

    yin: WidgetSchema = WidgetSchema(widget_id=1, name="Yin", purpose="thing 1")
    await WidgetService.create(yin, session)
    results: List[Widget] = session.query(Widget).all()

    assert len(results) == 1

    for k in yin.dict().keys():
        assert getattr(results[0], k) == getattr(yin, k)
