from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.finding import Finding
from app.models.host import Host
from app.schemas.finding import FindingCreate, FindingRead
from app.enums import Severity

router = APIRouter(prefix="/findings", tags=["findings"])


@router.post("/", response_model=FindingRead, status_code=status.HTTP_201_CREATED)
def create_finding(payload: FindingCreate, db: Session = Depends(get_db)):
    """Create a new finding against a host."""
    host = db.query(Host).filter(Host.id == payload.host_id).first()
    if not host:
        raise HTTPException(
            status_code=404,
            detail=f"Host with id {payload.host_id} not found",
        )

    finding = Finding(**payload.model_dump())
    db.add(finding)
    db.commit()
    db.refresh(finding)
    return finding


@router.get("/", response_model=List[FindingRead])
def list_findings(
    host_id: Optional[int] = None,
    severity: Optional[Severity] = None,
    db: Session = Depends(get_db),
):
    """
    Return all findings. Filter by host_id and/or severity via query string:
    /findings/?host_id=1
    /findings/?severity=critical
    /findings/?host_id=1&severity=high
    """
    query = db.query(Finding)
    if host_id is not None:
        query = query.filter(Finding.host_id == host_id)
    if severity is not None:
        query = query.filter(Finding.severity == severity.value)
    return query.order_by(Finding.created_at.desc()).all()


@router.get("/{finding_id}", response_model=FindingRead)
def get_finding(finding_id: int, db: Session = Depends(get_db)):
    """Return a single finding by ID."""
    finding = db.query(Finding).filter(Finding.id == finding_id).first()
    if not finding:
        raise HTTPException(status_code=404, detail="Finding not found")
    return finding