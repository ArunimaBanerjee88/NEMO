import sqlite3
from database import get_db

def get_user_state(user_id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT current_letter, stage FROM learning_state WHERE user_id=?",
        (user_id,)
    )
    row = cur.fetchone()
    conn.close()

    return row if row else ("A", "phonics")

def update_user_state(user_id, letter, stage):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO learning_state
    (user_id, current_letter, stage)
    VALUES (?, ?, ?)
    """, (user_id, letter, stage))

    conn.commit()
    conn.close()
