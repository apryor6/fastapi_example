from app.db import get_db, Session
from typing import List

from fastapi import Depends

from .model import Widget
from .schema import WidgetSchema


class WidgetService:
    @staticmethod
    def get_all(session: Session) -> List[Widget]:
        return session.query(Widget).all()
        # return Widget.query.all()

    # @staticmethod
    # def get_by_id(widget_id: int, db: Session = Depends(get_db)) -> Widget:
    #     return Widget.query.get(widget_id)

    # @staticmethod
    # def update(
    #     widget: Widget,
    #     Widget_change_updates: WidgetSchema,
    #     db: Session = Depends(get_db),
    # ) -> Widget:
    #     widget.update(Widget_change_updates)
    #     db.session.commit()
    #     return widget

    # @staticmethod
    # def delete_by_id(widget_id: int, db: Session = Depends(get_db)) -> List[int]:
    #     widget = Widget.query.filter(Widget.widget_id == widget_id).first()
    #     if not widget:
    #         return []
    #     db.session.delete(widget)
    #     db.session.commit()
    #     return [widget_id]

    @staticmethod
    def create(new_attrs: WidgetSchema, session: Session) -> WidgetSchema:
        new_widget = Widget(**new_attrs.dict())

        print("new_widget.__dict__")
        print(new_widget.__dict__)
        session.add(new_widget)
        session.commit()
        session.refresh(new_widget)
        print("new_widget.__dict__")
        print(new_widget.__dict__)
        return WidgetSchema(**new_widget.__dict__)

