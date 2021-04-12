import sqlite3
from datetime import datetime

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
    #cursor.execute("INSERT INTO users VALUES ('chen','123','admin','')")

    conn.commit()

from datetime import datetime

"""
# current date and time
now = datetime.now()

timestamp = int(datetime.timestamp(now))
time = datetime.fromtimestamp(timestamp)
"""