import sqlite3
from pathlib import Path

# Connection to the database
DB_PATH = Path("focustokens.db")

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn