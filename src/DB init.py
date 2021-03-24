import sqlite3

conn = sqlite3.connect("usersDB.db")
cursor = conn.cursor()
#DB init table
def db_init():
    cursor.execute("""CREATE TABLE users
                (userName text,
                pass text,
                type text,
                parent)""")  # type is admin , parent or kid
    #db insert rows
    cursor.execute("INSERT INTO users VALUES ('itay','123','admin','')")
    cursor.execute("INSERT INTO users VALUES ('yaron','123','parent','')")
    cursor.execute("INSERT INTO users VALUES ('chen','123','kid','yaron')")
    cursor.execute("INSERT INTO users VALUES ('yaniv','123','kid','yaron')")
    conn.commit()

db_init()
