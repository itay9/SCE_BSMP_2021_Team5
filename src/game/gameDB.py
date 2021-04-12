import sqlite3
from datetime import datetime

connKids = sqlite3.connect("KidsDB.db")
cursorKids = connKids.cursor()
connQ = sqlite3.connect("questionDB.db")
cursorQ = connQ.cursor()

#DB init table
def init_kidDB():
    cursorKids.execute("""CREATE TABLE users
                (KidName text,
                Date timestamp,
                GameNumber INTEGER,
                GameLog Blob,
                GameSuccess Real)""")
    #gamalog = [(Qnumber,answer,correct)]*
    #GameSuccess = (number of correct / total Q) * 100 %
    #db insert rows
    #cursor.execute("INSERT INTO users VALUES ('chen','123','admin','')")

def init_QDB():
    cursorQ.execute("""CREATE TABLE users
                (QuestionID INTEGER,
                Quesion text,
                picture blob,
                choice1 text,
                choice2 text,
                choice3 text,
                choice4 text,
                answer INTEGER)""")

    connQ.commit()

def get_question(question):
    cursorQ.execute()

def stampToTime(timestamp):
    return datetime.fromtimestamp(timestamp)

def timeToStamp(time):
    return int(datetime.timestamp(time))
