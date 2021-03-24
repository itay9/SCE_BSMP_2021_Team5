import sqlite3

conn = sqlite3.connect("testDB.db")
cursor = conn.cursor()

def login(user,password):
    cursor.execute("SELECT * FROM users WHERE userName = '"+user+"'")
    fet = cursor.fetchone()
    if fet is None:
        print("user does not exist!")
        return False
    else:
        if fet[1] == password:
            print("login succss!")
            return True
        else:
            print("wrong password!")
            return False




