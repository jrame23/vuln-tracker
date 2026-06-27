from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Engagement(Base):
    __tablename__ = "engagements"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    client = Column(String(200), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    status = Column(String(50), nullable=False, default="planning")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # One engagement has many hosts
    hosts = relationship("Host", back_populates="engagement", cascade="all, delete-orphan")