import sqlite3

conn = sqlite3.connect("testDB.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE type = 'admin'")
print("the admin is:",cursor.fetchone())

cursor.execute("SELECT * FROM users WHERE type = 'parent'")
print("the parent is:",cursor.fetchone())

cursor.execute("SELECT * FROM users WHERE type = 'kid'")
print("the kid are:",cursor.fetchall())


