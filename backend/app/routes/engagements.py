from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.engagement import Engagement
from app.schemas.engagement import EngagementCreate, EngagementRead

router = APIRouter(prefix="/engagements", tags=["engagements"])


@router.post("/", response_model=EngagementRead, status_code=status.HTTP_201_CREATED)
def create_engagement(payload: EngagementCreate, db: Session = Depends(get_db)):
    """Create a new engagement."""
    engagement = Engagement(**payload.model_dump())
    db.add(engagement)
    db.commit()
    db.refresh(engagement)
    return engagement


@router.get("/", response_model=List[EngagementRead])
def list_engagements(db: Session = Depends(get_db)):
    """Return all engagements."""
    return db.query(Engagement).order_by(Engagement.created_at.desc()).all()


@router.get("/{engagement_id}", response_model=EngagementRead)
def get_engagement(engagement_id: int, db: Session = Depends(get_db)):
    """Return a single engagement by ID."""
    engagement = db.query(Engagement).filter(Engagement.id == engagement_id).first()
    if not engagement:
        raise HTTPException(status_code=404, detail="Engagement not found")
    return engagement