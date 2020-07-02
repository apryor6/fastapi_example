from typing import List

import pytest

from app.test.fixtures import app, session  # noqa
from app.db import Session
from .model import Fizz
from .service import FizzService  # noqa
from .schema import FizzSchema


@pytest.mark.asyncio
async def test_get_all(session: Session):  # noqa
    yin: FizzSchema = FizzSchema(fizz_id=1, name="Yin", purpose="thing 1")
    yang: FizzSchema = FizzSchema(fizz_id=2, name="Yang", purpose="thing 2")
    session.add(Fizz(**yin.dict()))
    session.add(Fizz(**yang.dict()))
    session.commit()

    results: List[FizzSchema] = await FizzService.get_all(session)

    assert len(results) == 2
    assert yin in results and yang in results


@pytest.mark.asyncio
async def test_update(session: Session):  # noqa
    yin: FizzSchema = FizzSchema(fizz_id=1, name="Yin", purpose="thing 1")
    yin_orm = Fizz(**yin.dict())
    session.add(yin_orm)
    updates: FizzSchema = FizzSchema(fizz_id=1, name="New Fizz name", purpose="thing 1")

    await FizzService.update(yin_orm, updates, session)
    result: FizzSchema = session.query(Fizz).get(yin.fizz_id)
    assert result.name == "New Fizz name"


@pytest.mark.asyncio
async def test_delete_by_id(session: Session):  # noqa
    yin: FizzSchema = FizzSchema(fizz_id=1, name="Yin", purpose="thing 1")
    yang: FizzSchema = FizzSchema(fizz_id=2, name="Yang", purpose="thing 2")

    yin_orm = Fizz(**yin.dict())
    yang_orm = Fizz(**yang.dict())

    session.add(yin_orm)
    session.add(yang_orm)
    session.commit()

    await FizzService.delete_by_id(1, session)
    session.commit()

    results: List[Fizz] = session.query(Fizz).all()

    assert len(results) == 1
    assert yin_orm not in results and yang_orm in results


@pytest.mark.asyncio
async def test_create(session: Session):  # noqa

    yin: FizzSchema = FizzSchema(fizz_id=1, name="Yin", purpose="thing 1")
    await FizzService.create(yin, session)
    results: List[Fizz] = session.query(Fizz).all()

    assert len(results) == 1

    for k in yin.dict().keys():
        assert getattr(results[0], k) == getattr(yin, k)
