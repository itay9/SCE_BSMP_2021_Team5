import sqlite3

conn = sqlite3.connect("KidsDB.db")
cursor = conn.cursor()

#DB init table
def db_init():
    cursor.execute("""CREATE TABLE users
                (KidName text,
                Date timestamp,
                GameNumber INTEGER,
                GameLog Blob
                GameSuccess Real)""")
    #gamalog = [(Qnumber,answer,correct)]*
    #GameSuccess = (number of correct / total Q) * 100 %
    #db insert rows
    #cursor.execute("INSERT INTO users VALUES ('itay','123','admin','')")

    conn.commit()