from src.data.db import get_connection

# Creates the tables of the database
def create_tables() -> None:
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE  
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS token_balances (
            user_id INTEGER PRIMARY KEY,
            balance INTEGER NOT NULL,
            last_refresh DATE NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );    
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            daily_tokens INTEGER NOT NULL,
            normal_ping_cost INTEGER NOT NULL,
            urgent_ping_cost INTEGER NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS pings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_user_id INTEGER NOT NULL,
            receiver_user_id INTEGER NOT NULL,
            ping_type TEXT NOT NULL,
            message TEXT,
            cost INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (sender_user_id) REFERENCES users(id),
            FOREIGN KEY (receiver_user_id) REFERENCES users(id)
        );
        """)

        conn.commit()