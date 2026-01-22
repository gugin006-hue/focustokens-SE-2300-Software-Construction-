from datetime import date
from src.data.db import get_connection

def create_user(username: str) -> None:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (username,))
        conn.commit()