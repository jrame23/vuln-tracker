from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class EngagementBase(BaseModel):
    """Shared fields used by both create and read schemas."""
    name: str = Field(..., min_length=1, max_length=200)
    client: str = Field(..., min_length=1, max_length=200)
    start_date: date
    end_date: Optional[date] = None
    status: str = Field(default="planning", max_length=50)


class EngagementCreate(EngagementBase):
    """Schema for creating a new engagement (incoming POST body)."""
    pass


class EngagementRead(EngagementBase):
    """Schema for returning an engagement to the client (outgoing response)."""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Lets Pydantic read from SQLAlchemy objects