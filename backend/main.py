from fastapi import FastAPI

from app.database import engine, Base
from app.models import engagement, host, finding
from app.routes import engagements, hosts

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vulnerability Tracker API",
    description="Backend API for tracking penetration testing findings",
    version="0.1.0",
)

app.include_router(engagements.router)
app.include_router(hosts.router)


@app.get("/")
def read_root():
    return {"message": "Vulnerability Tracker API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}