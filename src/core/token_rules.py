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
    
def should_refresh(last_refresh: date, today: date) -> bool:
    if today > last_refresh:
        return True
    else:
        return False

def refresh_balance_if_needed(balance: int, daily_tokens: int, last_refresh: date, today: date) -> tuple[int, date]:
    if should_refresh(last_refresh, today):
        return (daily_tokens, today)
    else:
        return (balance, last_refresh)