import sqlite3
from datetime import datetime

conn = sqlite3.connect("networking.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        firm TEXT,
        role TEXT,
        email TEXT,
        how_met TEXT,
        date_met TEXT,
        last_contacted TEXT,
        notes TEXT
    )
""")

conn.commit()
conn.close()

date_met = datetime.now().strftime("%Y-%m-%d")

def add_contact(name, firm, role, email, how_met, notes):
    conn = sqlite3.connect("networking.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO contacts (name, firm, role, email, how_met, date_met, last_contacted, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, firm, role, email, how_met, date_met, date_met, notes))
    
    conn.commit()
    conn.close()