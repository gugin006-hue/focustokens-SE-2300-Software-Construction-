from __future__ import annotations

from dataclasses import dataclass
from datetime import date

# Sets the rules for token
@dataclass(frozen=True)
class SpendResult:
    new_balance: int
    success: bool
    reason: str | None = None

# Returns if the balance is enough to send a ping
def can_spend(balance: int, cost: int) -> bool:
    if cost >= 1 and balance >= cost:
        return True
    return False

# Returns the balance if success is True
def spend(balance: int, cost: int) -> SpendResult:
    if cost < 1:
        return SpendResult(new_balance=balance, success=False, reason="invalid_cost")
    elif balance < cost:
        return SpendResult(new_balance=balance, success=False, reason="insufficient_tokens")
    else:
        return SpendResult(new_balance=balance - cost, success=True, reason=None)
    
# Returns True if the day has passed and it's a new date
def should_refresh(last_refresh: date, today: date) -> bool:
    if today > last_refresh:
        return True
    else:
        return False

# Updates the token balance if should_refresh is True
def refresh_balance_if_needed(balance: int, daily_tokens: int, last_refresh: date, today: date) -> tuple[int, date]:
    if should_refresh(last_refresh, today):
        return (daily_tokens, today)
    else:
        return (balance, last_refresh)