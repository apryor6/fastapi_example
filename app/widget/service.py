from app.db import get_db, Session
from typing import List

from fastapi import Depends

from .model import Widget
from .schema import WidgetSchema


class WidgetService:
    @staticmethod
    async def get_all(session: Session) -> List[WidgetSchema]:
        resp = session.query(Widget).all()
        return [WidgetSchema(**i.__dict__) for i in resp]

    @staticmethod
    async def get_by_id(widget_id: int, session: Session) -> WidgetSchema:
        resp = session.query(Widget).get(widget_id)
        return WidgetSchema(**resp.__dict__)

    @staticmethod
    async def update(
        widget: Widget, updates: WidgetSchema, session: Session,
    ) -> WidgetSchema:
        widget.update(updates)
        session.commit()
        session.refresh(widget)
        return widget

    @staticmethod
    async def delete_by_id(widget_id: int, session: Session) -> List[int]:
        widget = session.query(Widget).filter(Widget.widget_id == widget_id).first()
        if not widget:
            return []
        session.delete(widget)
        session.commit()
        return [widget_id]

    @staticmethod
    async def create(new_attrs: WidgetSchema, session: Session) -> WidgetSchema:
        new_widget = Widget(**new_attrs.dict())

        session.add(new_widget)
        session.commit()
        session.refresh(new_widget)
        return WidgetSchema(**new_widget.__dict__)

