from fastapi import FastAPI

from .api.router import router
from .config import settings

app = FastAPI()

app.include_router(router, prefix="/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)
