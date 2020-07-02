from typing import List

from fastapi import Depends, APIRouter

from app.db import Session, get_db
from .schema import WidgetSchema
from .service import WidgetService
from .model import Widget

router = APIRouter()


@router.get("/")
async def get_widget(session: Session = Depends(get_db)) -> List[Widget]:
    """Get all Widgets"""
    return WidgetService.get_all(session)


@router.post(
    "/", response_model=WidgetSchema,
)
async def post_widget(
    widget: WidgetSchema, session: Session = Depends(get_db),
) -> WidgetSchema:
    """Create a new Widget"""
    print(f"widget = {widget}")
    print("Posting a widget")
    resp = WidgetService.create(widget, session)
    print(resp)
    return resp
    # return WidgetService.create(widget, session)


# @router.route("/<int:widget_id>")
# class widget_idResource(Resource):
#     @responds(schema=WidgetSchema)
#     def get(self, widget_id: int) -> Widget:
#         """Get Single Widget"""

#         return WidgetService.get_by_id(widget_id)

#     def delete(self, widget_id: int) -> Response:
#         """Delete Single Widget"""
#         from flask import jsonify

#         id = WidgetService.delete_by_id(widget_id)
#         return jsonify(dict(status="Success", id=id))

#     @accepts(schema=WidgetSchema, api=api)
#     @responds(schema=WidgetSchema)
#     def put(self, widget_id: int) -> Widget:
#         """Update Single Widget"""

#         changes: WidgetInterface = request.parsed_obj
#         Widget = WidgetService.get_by_id(widget_id)
#         return WidgetService.update(Widget, changes)
