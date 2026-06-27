from fastapi import FastAPI

app = FastAPI(
    title="Vulnerability Tracker API",
    description="Backend API for tracking penetration testing findings",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Vulnerability Tracker API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}