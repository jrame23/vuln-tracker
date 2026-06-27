from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True, index=True)
    host_id = Column(Integer, ForeignKey("hosts.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(300), nullable=False)
    description = Column(Text, nullable=False)
    severity = Column(String(20), nullable=False)
    cvss_score = Column(Numeric(3, 1), nullable=True)
    status = Column(String(50), nullable=False, default="open")
    evidence = Column(Text, nullable=True)
    remediation = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Many findings belong to one host
    host = relationship("Host", back_populates="findings")