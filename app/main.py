from fastapi import FastAPI
from app.routes import items, users

app = FastAPI(
    title="My API",
    description="A simple FastAPI application",
    version="0.1.0"
)

# Include routers
app.include_router(items.router)
app.include_router(users.router)


@app.get("/")
def hello_index():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
