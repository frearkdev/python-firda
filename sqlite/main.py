from datetime import date
import sqlite3

conn = sqlite3.connect("logboek.db")
cursor = conn.cursor()

datum = date.today().isoformat()
titel = input("Titel: ")
bericht = input("Bericht: ")
stemming = input("Stemming: ")

cursor.execute("""
INSERT INTO logboek (datum, titel, bericht, stemming)
VALUES (?, ?, ?, ?)
""", (datum, titel, bericht, stemming))

conn.commit()
conn.close()

print("Logboek item is opgeslagen")