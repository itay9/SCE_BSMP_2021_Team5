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

def register_parent():
    user = input("enter user name: ")
    cursor.execute("SELECT * FROM users WHERE userName = '" + user + "'")
    fet = cursor.fetchone()
    if fet is None:
        password = input("enter password: ")
        cursor.execute("INSERT INTO users VALUES ('"+user+"','"+password+"','parent')")
        print("register parent complete!")
        #TODO register new user
    else:
        print("user already exist!, select diffrent user name!")

def register_kid():
    user = input("enter user name: ")
    cursor.execute("SELECT * FROM users WHERE userName = '" + user + "'")
    fet = cursor.fetchone()
    if fet is None:
        password = input("enter password: ")
        cursor.execute("INSERT INTO users VALUES ('"+user+"','"+password+"','kid')")
        print("register kid complete!")
    else:
        print("user already exist!, select diffrent user name!")
register_parent()
