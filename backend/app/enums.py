from enum import Enum


class Severity(str, Enum):
    """CVSS-aligned severity levels for findings."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class FindingStatus(str, Enum):
    """Lifecycle status of a finding."""
    OPEN = "open"
    CONFIRMED = "confirmed"
    REMEDIATED = "remediated"
    ACCEPTED = "accepted"