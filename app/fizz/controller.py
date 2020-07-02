from typing import List

from fastapi import Depends, APIRouter

from app.db import Session, get_db
from .schema import FizzSchema
from .service import FizzService
from .model import Fizz

router = APIRouter()


@router.get("/", response_model=List[FizzSchema])
async def get_fizz(session: Session = Depends(get_db)) -> List[Fizz]:
    """Get all Fizzs"""
    return await FizzService.get_all(session)


@router.post(
    "/", response_model=FizzSchema,
)
async def post_fizz(
    fizz: FizzSchema, session: Session = Depends(get_db),
) -> FizzSchema:
    """Create a new Fizz"""
    return await FizzService.create(fizz, session)


@router.get("/<int:fizz_id>", response_model=FizzSchema)
async def get_fizz_by_id(fizz_id: int, session: Session = Depends(get_db)) -> Fizz:
    """Get Single Fizz"""

    return await FizzService.get_by_id(fizz_id, session)


@router.delete("/<int:fizz_id>")
async def delete(fizz_id: int, session: Session = Depends(get_db)):
    """Delete Single Fizz"""
    _id = await FizzService.delete_by_id(fizz_id, session)
    return dict(status="Success", id=_id)


@router.put("/<int:fizz_id>")
async def put(fizz: FizzSchema, session: Session = Depends(get_db)) -> FizzSchema:
    """Update Single Fizz"""
    cur_fizz = session.query(Fizz).get(fizz.fizz_id)
    return await FizzService.update(cur_fizz, fizz, session)
