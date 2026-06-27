\# Database Schema



\## Overview

The vulnerability tracker models a hierarchy used in real penetration testing engagements:

Engagement ---< Host ---< Finding

One engagement contains many hosts. Each host has many findings. Each finding has a severity rating.



\## Tables



\### engagements

A scoped security assessment.



| Column | Type | Notes |

|---|---|---|

| id | SERIAL | Primary key |

| name | VARCHAR(200) | Engagement name |

| client | VARCHAR(200) | Client organization |

| start\_date | DATE | When the engagement began |

| end\_date | DATE | When the engagement ended (nullable — engagement may be active) |

| status | VARCHAR(50) | `planning`, `active`, `reporting`, `closed` |

| created\_at | TIMESTAMP | Auto-set on insert |



\### hosts

A target system within an engagement's scope.



| Column | Type | Notes |

|---|---|---|

| id | SERIAL | Primary key |

| engagement\_id | INTEGER | Foreign key → engagements.id |

| hostname | VARCHAR(255) | Hostname or label |

| ip\_address | VARCHAR(45) | IPv4 or IPv6 (45 chars covers IPv6) |

| operating\_system | VARCHAR(100) | OS detection result, nullable |

| notes | TEXT | Free-form notes, nullable |

| created\_at | TIMESTAMP | Auto-set on insert |



\### findings

A specific vulnerability or weakness discovered.



| Column | Type | Notes |

|---|---|---|

| id | SERIAL | Primary key |

| host\_id | INTEGER | Foreign key → hosts.id |

| title | VARCHAR(300) | Short finding title |

| description | TEXT | Detailed write-up |

| severity | VARCHAR(20) | `critical`, `high`, `medium`, `low`, `info` |

| cvss\_score | DECIMAL(3,1) | 0.0–10.0, nullable |

| status | VARCHAR(50) | `open`, `confirmed`, `remediated`, `accepted` |

| evidence | TEXT | Proof of concept, screenshots refs, nullable |

| remediation | TEXT | Suggested fix, nullable |

| created\_at | TIMESTAMP | Auto-set on insert |



\## Severity Levels (CVSS-Aligned)



| Severity | CVSS Range | Meaning |

|---|---|---|

| Critical | 9.0–10.0 | Immediate exploitation, severe impact |

| High | 7.0–8.9 | Significant risk, prompt remediation needed |

| Medium | 4.0–6.9 | Moderate risk |

| Low | 0.1–3.9 | Minor risk |

| Info | 0.0 | Informational, no direct risk |

