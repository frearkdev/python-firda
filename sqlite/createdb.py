import sqlite3

conn = sqlite3.connect("logboek.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logboek (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datum TEXT,
    titel TEXT,
    bericht TEXT,
    stemming TEXT
)
""")

conn.commit()
print("Database en tabel zijn klaar!")