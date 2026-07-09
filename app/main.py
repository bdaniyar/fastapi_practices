from fastapi import FastAPI
from app.routes import items, users
from app.core import models
from contextlib import asynccontextmanager
from app.api_v1 import router as router_v1
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    

app = FastAPI(
    title="My API",
    description="A simple FastAPI application",
    version="0.1.0",
    lifespan=lifespan
)

# Include routers
app.include_router(items.router)
app.include_router(users.router)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def hello_index():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
