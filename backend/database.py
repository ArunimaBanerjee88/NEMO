import sqlite3

DB_NAME = "users.db"

def get_db():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()

    # Users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password_hash TEXT,
        google_id TEXT
    )
    """)


    # Chats table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        role TEXT,
        message TEXT,
        timestamp TEXT
    )
    """)

    # Learning state
    cur.execute("""
    CREATE TABLE IF NOT EXISTS learning_state (
        user_id INTEGER PRIMARY KEY,
        current_letter TEXT DEFAULT 'A',
        stage TEXT DEFAULT 'phonics'
    )
    """)

    conn.commit()
    conn.close()
