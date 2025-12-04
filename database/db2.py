import sqlite3
import os

print("БД:", os.path.abspath("allbase.db"))


DB_NAME = r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\database\allbase.db"

def get_connection():
    return sqlite3.connect(DB_NAME)                     

def add_user(name, iin, score, time, wrong):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, iin, score, time, wrong ) VALUES (?, ?, ?, ? ,?)",
        (name, iin, score, time, wrong)
    )
    conn.commit()
    conn.close()

def get_user_by_iin(iin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, iin, score, time, wrong FROM users WHERE iin = ?",
        (iin,)
    )
    users = cursor.fetchall()   # ← БАРЛЫҚ жолдарды алады
    conn.close()
    return users



def cleanup_results(iin):
    conn = get_connection()
    cur = conn.cursor()

    # 1. Соңғы 3 жазбаның ID-сін алу
    cur.execute("""
        SELECT id FROM users
        WHERE iin = ?
        ORDER BY id DESC
        LIMIT 3
    """, (iin,))
    last_three = [row[0] for row in cur.fetchall()]

    # Егер 3-тен аз болса — өшірудің қажеті жоқ
    if len(last_three) < 3:
        conn.close()
        return

    # 2. Қалған ескілерін өшіру
    cur.execute(f"""
        DELETE FROM users
        WHERE iin = ?
        AND id NOT IN ({','.join(['?'] * len(last_three))})
    """, (iin, *last_three))

    conn.commit()
    conn.close()
