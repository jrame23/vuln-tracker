import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from .env file
load_dotenv()

# Read the database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your .env file.")

# The engine is SQLAlchemy's core interface to the database
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal is a factory for database sessions.
# Each request will get its own session to talk to the DB.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that all our models will inherit from
Base = declarative_base()


def get_db():
    """
    Dependency that yields a database session and ensures it's closed.
    FastAPI will inject this into endpoints that need DB access.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()