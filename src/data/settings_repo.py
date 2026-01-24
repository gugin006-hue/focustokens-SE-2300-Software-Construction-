from sqlite3 import Row
from src.data.db import get_connection

# Assigns default values to settings
def ensure_default_settings() -> None:
    daily_tokens = 10
    normal_ping_cost = 1
    urgent_ping_cost = 3
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO settings (id, daily_tokens, normal_ping_cost, urgent_ping_cost) VALUES (?, ?, ?, ?)", (1, daily_tokens, normal_ping_cost, urgent_ping_cost))
        conn.commit()

# Returns the settings tuple
def get_settings() -> Row:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM settings WHERE id = 1")
        row = cur.fetchone()
        return row
