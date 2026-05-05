from fastapi import FastAPI
from app.routes import health, execute, users, services, payments, whatsapp, jobs

app = FastAPI(title="Solutions Agent Platform API")

app.include_router(health.router)
app.include_router(execute.router)
app.include_router(users.router)
app.include_router(services.router)
app.include_router(payments.router)
app.include_router(whatsapp.router)
app.include_router(jobs.router)
