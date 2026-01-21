from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SpendResult:
    new_balance: int
    success: bool
    reason: str | None = None