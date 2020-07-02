from app.db import get_db, Session
from typing import List

from fastapi import Depends

from .model import Fizz
from .schema import FizzSchema


class FizzService:
    @staticmethod
    async def get_all(session: Session) -> List[FizzSchema]:
        resp = session.query(Fizz).all()
        return [FizzSchema(**i.__dict__) for i in resp]

    @staticmethod
    async def get_by_id(fizz_id: int, session: Session) -> FizzSchema:
        resp = session.query(Fizz).get(fizz_id)
        return FizzSchema(**resp.__dict__)

    @staticmethod
    async def update(fizz: Fizz, updates: FizzSchema, session: Session,) -> FizzSchema:
        fizz.update(updates)
        session.commit()
        session.refresh(fizz)
        return fizz

    @staticmethod
    async def delete_by_id(fizz_id: int, session: Session) -> List[int]:
        fizz = session.query(Fizz).filter(Fizz.fizz_id == fizz_id).first()
        if not fizz:
            return []
        session.delete(fizz)
        session.commit()
        return [fizz_id]

    @staticmethod
    async def create(new_attrs: FizzSchema, session: Session) -> FizzSchema:
        new_fizz = Fizz(**new_attrs.dict())

        session.add(new_fizz)
        session.commit()
        session.refresh(new_fizz)
        return FizzSchema(**new_fizz.__dict__)

