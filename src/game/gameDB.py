import sqlite3
from datetime import datetime
import random

conn = sqlite3.connect("GameDB.db")
cursor = conn.cursor()

# DB init table
def init_QDB():
    cursor.execute("""CREATE TABLE ques
                (qid INTEGER,
                quesion text,
                picture text,
                choice1 text,
                choice2 text,
                choice3 text,
                choice4 text,
                answer INTEGER)""")
    conn.commit()
    add_question_to_qdb("banana", "pic/banana.jpg", 1, 2, 3, 4, 1)
    add_question_to_qdb("apple", "aurl", 1, 2, 3, 4, 2)
    add_question_to_qdb("Pineapple", "pine url", 1, 2, 3, 4, 4)
    add_question_to_qdb("tomato", "tomato url", 1, 2, 3, 4, 4)

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

def init_game_log_DB():
    '''
    init game result DB
    0: KidName
    1: GameNumber
    2: qid
    3: playerAns
    Returns: build db

    '''
    cursor.execute("""CREATE TABLE gameLog
                    (KidName text,
                    GameNumber INTEGER,
                    qid INTEGER,
                    playerAns INTEGER)""")

def add_result_to_gameLog(KidName,GameNumber,qid,playerAns):
    '''
    add gmaelog data after game
    Args:
        KidName:
        GameNumber:
        qid:
        playerAns:

    Returns:

    '''
    data = (KidName,GameNumber,qid,playerAns)
    cursor.execute("INSERT INTO gameLog VALUES (?,?,?,?)",data)
    conn.commit()
    print("result add to DB")

def add_result_to_Kidsdb(kidName, date, gameLog, gameSuccess):
    cursor.execute("INSERT into results VALUES (?,?,?,?,?)",
                   (kidName, date, get_game_number(kidName) + 1, gameLog, gameSuccess))
    conn.commit()
    print("result add to DB")

def add_question_to_qdb(question, picUrl, ch1, ch2, ch3, ch4, ans):
    # check if question already exist (by 'question')

    cursor.execute("INSERT INTO ques VALUES (?,?,?,?,?,?,?,?)",
                   (get_qestion_id(), question, picUrl, ch1, ch2, ch3, ch4, ans))
    conn.commit()
    print("question added")

def get_question_from_id(questionID):
    # check if input is legal
    cursor.execute("SELECT * FROM ques WHERE qid = ?", (questionID,))  # send the INT as tuple is required
    fet = cursor.fetchone()
    if fet != None:
        return fet
    else:
        print("can't find question")
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
        return

def get_ans(qid):
    cursor.execute("SELECT answer FROM ques WHERE qid=?", (qid,))
    fet = cursor.fetchone()
    if fet != None:
        return fet[0] #fetchone return tuple
    else:
        return

def get_game_number(kidName):
    cursor.execute("SELECT * FROM results WHERE kidName=?", (kidName,))
    fet = cursor.fetchall()
    return len(fet)

def get_qestion_id():
    '''

    Returns: id for next questions

    '''
    cursor.execute("SELECT max(qid) FROM ques")
    fet = cursor.fetchone()
    #TODO fix None bug
    if fet !=None:
        return fet[0] + 1

def get_question_for_game(number_of_question):
    '''

    Args:
        number_of_question: number of questions

    Returns: list of questions

    '''
    if number_of_question == 0: return None
    print("get_question_for_game:")
    if number_of_question > get_qestion_id() - 1:
        # תיקון מספר השאלות
        print("number of question modify to max ques in DB")
        number_of_question = get_qestion_id() - 1
    # set the questions to list
    cursor.execute("SELECT * FROM ques")
    ques_list = cursor.fetchall()
    print("ques_list: ",len(ques_list))
    qList = []
    num_list = generate_rand_number_list(number_of_question)
    print("num_list", num_list)
    for i in num_list:
        qList.append(ques_list[i-1])
    return qList

def generate_rand_number_list(size):
    '''

    Args:
        size: int size of list

    Returns: list of random number for qid

    '''
    num_list = []
    for i in range(size):
        number = random.randint(1,size+1)
        while number in num_list:
            number = random.randint(1, size + 1)
        num_list.append(number)
    return num_list

def check_answer(qid,ans):
    '''

    Args:
        qid: int number of question
        ans: player answer

    Returns: True if ans correct
             False if ans wrong

    '''
    cursor.execute("SELECT * FROM ques WHERE qid=?",(qid,))
    fet = cursor.fetchone()
    if fet != None:
        true_ans = fet[7]
        if true_ans==ans:
            return True
        else:
            return False

def build_db():
    try:
        init_QDB()
        init_kidDB()
        init_game_log_DB()
    except:
        pass

def calc_game_success(kidName,gameNumber):
    '''

    Args:
        kidName: str of kid
        gameNumber: int of game

    Returns: game success rate

    '''
    correct_ans = 0
    param = (kidName,gameNumber)
    cursor.execute("SELECT * FROM gameLog WHERE kidName=? AND gameNumber = ?",param)
    fet = cursor.fetchall()
    for data in fet:
        if check_answer(data[2],data[3]):
            print(data[2],data[3])
            correct_ans+=1
    success_rate =  correct_ans/len(fet)
    return success_rate


add_question_to_qdb("Pineapple", "pine url", 1, 2, 3, 4, 4)
add_question_to_qdb("tomato", "tomato url", 1, 2, 3, 4, 4)