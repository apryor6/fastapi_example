from .model import Widget  # noqa
from .schema import WidgetSchema  # noqa

BASE_ROUTE = "widget"


def register_routes(app, root="api"):
    from .controller import router as widget_router

    app.include_router(widget_router, prefix=f"/{root}/{BASE_ROUTE}")
