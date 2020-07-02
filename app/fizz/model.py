from sqlalchemy import Integer, Column, String
from app.db import Base

from .schema import FizzSchema


class Fizz(Base):  # type: ignore
    """A snazzy Fizz"""

    __tablename__ = "fizz"

    fizz_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    purpose = Column(String(255))

    def update(self, changes: FizzSchema):
        for key, val in changes.dict().items():
            setattr(self, key, val)
        return self
