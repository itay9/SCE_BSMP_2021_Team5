import sqlite3
from datetime import datetime

conn = sqlite3.connect("GameDB.db")
cursor = conn.cursor()


# DB init table
def init_kidDB():
    cursor.execute("""CREATE TABLE results
                (KidName text,
                Date timestamp,
                GameNumber INTEGER,
                GameLog Blob,
                GameSuccess Real)""")
    # gamalog = [(Qnumber,answer,correct)]*
    # GameSuccess = (number of correct / total Q) * 100 %
    # db insert rows
    # cursor.execute("INSERT INTO users VALUES ('chen','123','admin','')")


def init_QDB():
    cursor.execute("""CREATE TABLE ques
                (qid INTEGER,
                quesion text,
                picture blob,
                choice1 text,
                choice2 text,
                choice3 text,
                choice4 text,
                answer INTEGER)""")

    conn.commit()


def get_question_from_id(questionID):
    cursor.execute("SELECT * FROM ques WHERE qid = ?", questionID)
    fet = cursor.fetchone()
    if fet != None:
        return fet
    else:
        print("cant find question")


def stampToTime(timestamp):
    return datetime.fromtimestamp(timestamp)


def timeToStamp(time):
    return int(datetime.timestamp(time))


def add_result_to_Kidsdb(kidName, date, gameNumber, gameLog, gameSuccess):
    cursor.execute("INSERT into results VALUES (?,?,?,?,?)", [kidName, date, gameNumber, gameLog, gameSuccess])
    print("result add to DB")

def get_kid_results(kidName):
    cursor.execute("SELECT * FROM results WHERE kidName = ?",kidName )
    fet = cursor.fetchall()
    if len(fet)!=0:
        return fet
    else:
        print("no result")
        return []

def add_question_to_qdb(quesion,picUrl,ch1,ch2,ch3,ch4,ans):
    cursor.execute("INSERT INTO ques VALUES (?,?,?,?,?,?,?)",[quesion,picUrl,ch1,ch2,ch3,ch4,ans])
    print("question added")

