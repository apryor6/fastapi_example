from sqlalchemy import Integer, Column, String
from app.db import Base

from .schema import WidgetSchema


class Widget(Base):  # type: ignore
    """A snazzy Widget"""

    __tablename__ = "widget"

    widget_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    purpose = Column(String(255))

    def update(self, changes: WidgetSchema):
        for key, val in changes.dict().items():
            setattr(self, key, val)
        return self
