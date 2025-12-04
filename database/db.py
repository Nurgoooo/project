import sqlite3
import os

print("БД:", os.path.abspath("databas32.db"))


DB_NAME = r"C:\Users\Asus\Desktop\Workspace\Nurait things\Python 3.13\py313\nur\projectbay\database\databas32.db"

def get_connection():
    return sqlite3.connect(DB_NAME)                     

def add_user(name, iin, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, iin, password ) VALUES (?, ?, ?)",
        (name, iin, password)
    )
    conn.commit()
    conn.close()

def get_user_by_iin(iin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, iin, password FROM users WHERE iin = ?",
        (iin,)
    )
    user = cursor.fetchone()
    conn.close()
    return user

def get_password_by_iin(iin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password FROM users WHERE iin = ?",
        (iin,)
    )
    password = cursor.fetchone()
    conn.close()
    return password    

def get_total_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )
    result = cursor.fetchone()
    conn.close()
    return result[0] 



