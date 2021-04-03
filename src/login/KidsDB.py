import sqlite3

conn = sqlite3.connect("KidsDB.db")
cursor = conn.cursor()

#DB init table
def db_init():
    cursor.execute("""CREATE TABLE users
                (userName text,
                Date timestamp,
                GameNumber INTEGER,
                GameLog Blob
                GameSuccess Real)""")  # type is admin , parent or kid
    #db insert rows
    #cursor.execute("INSERT INTO users VALUES ('itay','123','admin','')")

    conn.commit()