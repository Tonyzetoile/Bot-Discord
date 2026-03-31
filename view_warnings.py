import sqlite3

connection = sqlite3.connect("warnings.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM warnings;")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()