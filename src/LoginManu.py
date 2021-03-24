import sqlite3

conn = sqlite3.connect("testDB.db")
cursor = conn.cursor()
"""
cursor.execute("SELECT * FROM users WHERE type = 'admin'")
print("the admin is:",cursor.fetchone()[0])
"""
user = input("enter user name: ")
cursor.execute("SELECT * FROM users WHERE userName = '"+user+"'")
fet = cursor.fetchone()
if fet is None:
    print("user does not exist!")
else:
    password = input("enter password: ")
    if fet[1] == password:
        print("login succss!")
    else:
        print("wrong password!")
#teasdasd
#aasd


