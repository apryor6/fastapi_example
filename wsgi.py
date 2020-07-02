import os

from app import create_app

app = create_app(config=os.getenv("ENV") or "test")

