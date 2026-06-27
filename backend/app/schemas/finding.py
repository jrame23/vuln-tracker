from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, field_validator

from app.enums import Severity, FindingStatus


class FindingBase(BaseModel):
    """Shared fields for finding create and read schemas."""
    title: str = Field(..., min_length=1, max_length=300)
    description: str = Field(..., min_length=1)
    severity: Severity
    cvss_score: Optional[Decimal] = Field(default=None, ge=0.0, le=10.0)
    status: FindingStatus = FindingStatus.OPEN
    evidence: Optional[str] = None
    remediation: Optional[str] = None

    @field_validator("cvss_score")
    @classmethod
    def round_cvss(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        """CVSS scores are expressed to one decimal place."""
        if v is None:
            return v
        return Decimal(str(round(float(v), 1)))


class FindingCreate(FindingBase):
    """Schema for creating a new finding."""
    host_id: int


class FindingRead(FindingBase):
    """Schema for returning a finding to the client."""
    id: int
    host_id: int
    created_at: datetime

    class Config:
        from_attributes = True