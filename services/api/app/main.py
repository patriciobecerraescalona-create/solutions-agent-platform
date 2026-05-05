from fastapi import FastAPI
from app.routes import health, execute

app = FastAPI(title="Solutions Agent Platform API")

app.include_router(health.router)
app.include_router(execute.router)
