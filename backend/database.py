import sqlite3

def init_db():
    conn = sqlite3.connect("tourism.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tourists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            passport TEXT,
            hash TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tourist_hash TEXT,
            incident TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()
