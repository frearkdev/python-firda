import sqlite3

conn = sqlite3.connect("logboek.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM logboek")
items = cursor.fetchall()

for item in items:
    print(item)

conn.close()