import sqlite3
from datetime import datetime

def save_message(user_id, role, message):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO chats (user_id, role, message, timestamp) VALUES (?, ?, ?, ?)",
        (user_id, role, message, datetime.utcnow())
    )
    conn.commit()
    conn.close()

def get_chat_history(user_id, limit=50):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT role, message FROM chats WHERE user_id=? ORDER BY id ASC LIMIT ?",
        (user_id, limit)
    )
    rows = cur.fetchall()
    conn.close()
    return rows
