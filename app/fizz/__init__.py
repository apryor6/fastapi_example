from .model import Fizz  # noqa
from .schema import FizzSchema  # noqa

BASE_ROUTE = "fizz"


def register_routes(app, root="api"):
    from .controller import router as fizz_router

    app.include_router(fizz_router, prefix=f"/{root}/{BASE_ROUTE}")
