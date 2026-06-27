from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class HostBase(BaseModel):
    """Shared fields for host create and read schemas."""
    hostname: str = Field(..., min_length=1, max_length=255)
    ip_address: str = Field(..., min_length=1, max_length=45)
    operating_system: Optional[str] = Field(default=None, max_length=100)
    notes: Optional[str] = None


class HostCreate(HostBase):
    """Schema for creating a new host (incoming POST body)."""
    engagement_id: int


class HostRead(HostBase):
    """Schema for returning a host to the client."""
    id: int
    engagement_id: int
    created_at: datetime

    class Config:
        from_attributes = True