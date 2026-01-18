import hashlib
import sqlite3
from database import get_db

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(email: str, password: str):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (email, password_hash) VALUES (?, ?)",
            (email, hash_password(password))
        )
        conn.commit()
        return cur.lastrowid
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()

def login_user(email: str, password: str):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM users WHERE email=? AND password_hash=?",
        (email, hash_password(password))
    )

    row = cur.fetchone()
    conn.close()

    return row["id"] if row else None
