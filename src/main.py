from fastapi import FastAPI

from .api.router import router
from .config import settings

app = FastAPI()

app.include_router(router, prefix="/v1")

