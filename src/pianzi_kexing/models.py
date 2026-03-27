from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class WatchlistEntry:
    subject_id: str
    source_type: str
    source_url: str
    published_at: str
    jurisdiction: str
    legal_basis: str
    official_source_confirmed: bool
    supports_retraction: bool
    contains_biometric_template: bool
    uses_crowdsourced_accusation: bool
    status: str


@dataclass(slots=True)
class PolicyDecision:
    allowed: bool
    issues: list[str]
