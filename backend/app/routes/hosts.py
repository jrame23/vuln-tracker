from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.host import Host
from app.models.engagement import Engagement
from app.schemas.host import HostCreate, HostRead

router = APIRouter(prefix="/hosts", tags=["hosts"])


@router.post("/", response_model=HostRead, status_code=status.HTTP_201_CREATED)
def create_host(payload: HostCreate, db: Session = Depends(get_db)):
    """Create a new host within an engagement."""
    # Verify the engagement exists before creating the host
    engagement = db.query(Engagement).filter(Engagement.id == payload.engagement_id).first()
    if not engagement:
        raise HTTPException(
            status_code=404,
            detail=f"Engagement with id {payload.engagement_id} not found",
        )

    host = Host(**payload.model_dump())
    db.add(host)
    db.commit()
    db.refresh(host)
    return host


@router.get("/", response_model=List[HostRead])
def list_hosts(engagement_id: int | None = None, db: Session = Depends(get_db)):
    """
    Return all hosts. Optionally filter by engagement_id via query string:
    /hosts/?engagement_id=1
    """
    query = db.query(Host)
    if engagement_id is not None:
        query = query.filter(Host.engagement_id == engagement_id)
    return query.order_by(Host.created_at.desc()).all()


@router.get("/{host_id}", response_model=HostRead)
def get_host(host_id: int, db: Session = Depends(get_db)):
    """Return a single host by ID."""
    host = db.query(Host).filter(Host.id == host_id).first()
    if not host:
        raise HTTPException(status_code=404, detail="Host not found")
    return host