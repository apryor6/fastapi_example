from typing import Optional

from app.base import CamelModel


class WidgetSchema(CamelModel):
    """Widget schema"""

    widget_id: Optional[int]
    name: str
    purpose: str
