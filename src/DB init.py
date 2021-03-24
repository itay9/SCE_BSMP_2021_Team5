import sqlite3

conn = sqlite3.connect("testDB.db")
cursor = conn.cursor()
#DB init table
"""
cursor.execute(""CREATE TABLE users
            (userName text,
            pass text,
            type text)"")  # type is admin , parent or kid
cursor.execute("INSERT INTO users VALUES ('itay','123','admin')")
"""
#db insert rows
"""
cursor.execute("INSERT INTO users VALUES ('yaron','123','parent')")
cursor.execute("INSERT INTO users VALUES ('chen','123','kid')")
cursor.execute("INSERT INTO users VALUES ('yaniv','123','kid')")
conn.commit()
"""