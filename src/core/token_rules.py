from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class SpendResult:
    new_balance: int
    success: bool
    reason: str | None = None

def can_spend(balance: int, cost: int) -> bool:
    if cost >= 1 and balance >= cost:
        return True
    return False

def spend(balance: int, cost: int) -> SpendResult:
    if cost < 1:
        return SpendResult(new_balance=balance, success=False, reason="invalid_cost")
    elif balance < cost:
        return SpendResult(new_balance=balance, success=False, reason="insufficient_tokens")
    else:
        return SpendResult(new_balance=balance - cost, success=True, reason=None)