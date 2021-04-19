import sqlite3
from datetime import datetime

conn = sqlite3.connect("GameDB.db")
cursor = conn.cursor()


# DB init table
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
    add_question_to_qdb("banana", "burl", 1, 2, 3, 4, 1)
    add_question_to_qdb("apple", "aurl", 1, 2, 3, 4, 2)


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
    conn.commit()
    add_result_to_Kidsdb("chen", datetime.now(), 1, 23)
    add_result_to_Kidsdb("chen", datetime.now(), 0, 95)


def add_result_to_Kidsdb(kidName, date, gameLog, gameSuccess):
    cursor.execute("INSERT into results VALUES (?,?,?,?,?)",
                   (kidName, date, get_game_number(kidName) + 1, gameLog, gameSuccess))
    conn.commit()
    print("result add to DB")


def add_question_to_qdb(quesion, picUrl, ch1, ch2, ch3, ch4, ans):
    cursor.execute("INSERT INTO ques VALUES (?,?,?,?,?,?,?,?)",
                   (get_qestion_id(), quesion, picUrl, ch1, ch2, ch3, ch4, ans))
    conn.commit()
    print("question added")


def get_question_from_id(questionID):
    # check if input is legal
    cursor.execute("SELECT * FROM ques WHERE qid = ?", (questionID,))#send the INT as tuple is required
    fet = cursor.fetchone()
    if fet != None:
        return fet
    else:
        print("cant find question")
        return


def stampToTime(timestamp):
    return datetime.fromtimestamp(timestamp)


def timeToStamp(time):
    return int(datetime.timestamp(time))


def get_kid_results(kidName):
    cursor.execute("SELECT * FROM results WHERE kidName =?", (kidName,))
    fet = cursor.fetchall()
    if len(fet) != 0:
        return fet
    else:
        print("no result")
        return []


def get_ans(qid):
    cursor.execute("SELECT answer FROM ques WHERE qid=?", qid)
    fet = cursor.fetchone()
    if fet != None:
        return fet
    else:
        return 0


def get_game_number(kidName):
    cursor.execute("SELECT * FROM results WHERE kidName=?", (kidName,))
    fet = cursor.fetchall()
    return len(fet)


def get_qestion_id():
    cursor.execute("SELECT * FROM ques")
    fet = cursor.fetchall()
    return len(fet) + 1


def build_db():
    try:
        init_QDB()
    except:
        pass
