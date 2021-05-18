import sqlite3
import datetime
import random
import pandas as pd

conn = sqlite3.connect("GameDB.db")
cursor = conn.cursor()

currentUser = "defult"
sassionFlag = False


# DB init table
def init_userDB():
    cursor.execute("""CREATE TABLE users
                (userName text,
                pass text,
                type text, 
                parent text,
                canReg integer,
                canPlay integer)""")
    # type is admin , parent or kid
    # canReg : 1 True , 0 False
    # db insert rows
    cursor.execute("INSERT INTO users VALUES ('itay','123','admin','',1,0)")
    cursor.execute("INSERT INTO users VALUES ('yaron','123','parent','',1,0)")
    cursor.execute("INSERT INTO users VALUES ('chen','123','kid','yaron',0,1)")
    cursor.execute("INSERT INTO users VALUES ('yaniv','123','kid','yaron',0,1)")
    conn.commit()


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
    add_question_to_qdb("banana", "pic/banana.jpg", "banana", "apple", "pizza", "car", 1)
    add_question_to_qdb("apple", "pic/apple.jpg", "dad", "apple", "table", "dog", 2)
    add_question_to_qdb("pineapple", "pic/pineapple.jpg", "watermelon", "hair", "cat", "pineapple", 4)
    add_question_to_qdb("tomato", "pic/tomato.jpg", "cat", "dog", "window", "tomato", 4)


def init_kidDB():
    cursor.execute("""CREATE TABLE results
                (KidName text,
                Date text,
                GameNumber INTEGER,
                GameSuccess Real)""")
    # gamalog = [(Qnumber,answer,correct)] TODO remove this attribute
    # GameSuccess = (number of correct / total Q) * 100 %
    # db insert rows
    conn.commit()


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


def changeSassion(user):
    global currentUser
    global sassionFlag
    currentUser = user
    sassionFlag = True
    print(currentUser)


def logOut():
    global currentUser
    global sassionFlag
    currentUser = ""
    sassionFlag = False
    print("session clear")


def login(user, password):
    """
    Args:
        user: string
        password: string

    Returns: user if login ok
            error message user or pass

    """
    cursor.execute("SELECT * FROM users WHERE userName = '" + user + "'")
    fet = cursor.fetchone()
    if fet is None:
        print("user does not exist!")
        return "wrong user"
    else:
        if fet[1] == password:
            print("login succss!")
            changeSassion(fet[0])
            return fet[0]  # return user name
        else:
            print("wrong password!")
            return "Wrong password"


def register_parent(user, password):
    """

    Args:
        user: string
        password: string

    Returns: register parent to DB

    """
    if user != "":
        cursor.execute("SELECT * FROM users WHERE userName = '" + user + "'")
        fet = cursor.fetchone()
        if fet is None:
            cursor.execute("INSERT INTO users VALUES ('" + user + "','" + password + "','parent','None',0,0)")
            conn.commit()
            print("register parent complete!")
            return True
        else:
            print("user already exist!, select different user name!")
            return False


def register_kid(user, password, parent):
    """

    Args:
        user: name of the kid
        password:
        parent: name of parent

    Returns: register new kid to DB
        true if register ok
        false if not

    """
    if canRegister(parent):
        cursor.execute("SELECT * FROM users WHERE userName = '" + user + "'")
        fet = cursor.fetchone()
        if fet is None:
            cursor.execute("INSERT INTO users VALUES ('" + user + "','" + password + "','kid','" + parent + "',0,0)")
            conn.commit()
            print("register kid complete!")
            return True
        else:
            print("user already exist!, select different user name!")
            return False
    else:
        print("cant register!")
        return False


def register_admin(user, password):
    """

    Args:
        user:
        password:

    Returns:
        true if register ok
        false if not

    """
    cursor.execute("SELECT * FROM users WHERE userName = '" + user + "'")
    fet = cursor.fetchone()
    if fet is None:
        cursor.execute("INSERT INTO users VALUES ('" + user + "','" + password + "','admin','None',1,0)")  # new
        conn.commit()
        print("register admin complete!")
        return True
    else:
        print("user already exist!, select different user name!")
        return False


def get_kids(parent):
    """

    Args:
        parent:

    Returns: list of parent kids

    """
    if parent != "":
        cursor.execute("SELECT * FROM users WHERE parent='" + parent + "'")
        fet = cursor.fetchall()
        if len(fet) == 0:
            print(parent, "has no kids in the system!")
            return
        else:
            kids_list = []
            for kid in fet:
                kids_list.append(kid[0])
            return kids_list


def remove_user(user):
    """
    func to remove user from DB
    if have kids remove the kids
    Args:
        user: user to remove

    Returns:
        false if user not exsist
        True if exist

    """
    cursor.execute("SELECT * FROM users WHERE userName ='" + user + "'")
    fet = cursor.fetchone()
    if fet is None:
        print("user no exist")
        return False
    elif fet[2] == "parent":
        if get_kids(user) != None:
            for kid in get_kids(user):
                remove_user(kid)
    cursor.execute("DELETE FROM users WHERE userName= '" + user + "'")
    conn.commit()
    print(user, "removed")
    return True


def remove_question(qid):
    qid_tuple = (qid,)
    # print(type(qid_tuple))
    cursor.execute("SELECT * FROM ques WHERE qid =?", qid_tuple)
    fet = cursor.fetchone()
    if fet is None:
        print("question no exist")
        return False
    cursor.execute("DELETE FROM ques WHERE qid= ?", qid_tuple)
    conn.commit()
    print("question #", qid, " removed from QuesDB")


def get_type(user):
    """

    Args:
        user: string

    Returns: list of kids

    """
    cursor.execute("SELECT * FROM users WHERE userName ='" + user + "'")
    fet = cursor.fetchone()
    return fet[2]


def allowReg(parent):
    par_reg = getUser(parent)[4]
    if par_reg == 0:
        cursor.execute("UPDATE users SET canReg = 1 WHERE userName= ? ", (parent,))
    else:
        cursor.execute("UPDATE users SET canReg = 0 WHERE userName= ? ", (parent,))
    conn.commit()


def canRegister(user):
    if get_type(user) == "parent":
        if getUser(user)[4] == 1:
            return True
    elif get_type(user) == "admin":
        return True
    else:
        return False


def getUser(userName):
    cursor.execute("SELECT * FROM users WHERE userName = ?", (userName,))
    fet = cursor.fetchone()
    return fet


def get_number_of_users():
    """

    Returns: number of users for row in print table

    """
    cursor.execute("SELECT * FROM users")
    fet = cursor.fetchall()
    return len(fet)


# get data funcs
def get_data_all():
    '''

    Returns: all data INCLUDE ADMIN
            internal use only!

    '''
    cursor.execute("SELECT * FROM users")
    fet = cursor.fetchall()
    return fet


def get_data_all_users():
    '''

    Returns: all data except admin
    '''
    cursor.execute("SELECT * FROM users WHERE type NOT IN ('admin')")
    fet = cursor.fetchall()
    return fet


def get_data_kid_by_parent(parent):
    '''

    Args:
        parent: name of parent

    Returns: data from users of parent kids

    '''
    if parent != "":
        cursor.execute("SELECT * FROM users WHERE parent=?", (parent,))
        fet = cursor.fetchall()
        return fet


def get_data_parent():
    cursor.execute("SELECT * FROM users WHERE type='parent'")
    fet = cursor.fetchall()
    return fet


def get_data_kid():
    cursor.execute("SELECT * FROM users WHERE type='kid'")
    fet = cursor.fetchall()
    return fet


def allowPlay(kid):
    kid_allow = getUser(kid)[5]
    if kid_allow == 0:
        cursor.execute("UPDATE users SET canPlay = 1 WHERE userName= ? ", (kid,))
    else:
        cursor.execute("UPDATE users SET canPlay = 0 WHERE userName= ? ", (kid,))
    conn.commit()


def build_db():
    try:
        init_userDB()
        init_QDB()
        init_kidDB()
        init_game_log_DB()
    except:
        pass


def add_result_to_gameLog(KidName, GameNumber, qid, playerAns):
    '''
    add gmaelog data after game
    Args:
        KidName:
        GameNumber:
        qid:
        playerAns:

    Returns:

    '''
    data = (KidName, GameNumber, qid, playerAns)
    cursor.execute("INSERT INTO gameLog VALUES (?,?,?,?)", data)
    conn.commit()
    print("result add to Gamelog DB")


def add_result_to_Kidsdb(kidName):
    time = get_norm_time_now()
    game_number = get_next_game_number(kidName)
    suc_rate = calc_game_success(kidName, game_number)
    data = (kidName, time, game_number, suc_rate)
    # print(data)
    cursor.execute("INSERT into results VALUES (?,?,?,?)", data)
    conn.commit()
    print("result added to kids result DB")


def add_question_to_qdb(question, picUrl, ch1, ch2, ch3, ch4, ans):
    # check if question already exist (by 'question')
    data = (get_next_qestion_id(), question, picUrl, ch1, ch2, ch3, ch4, ans)
    cursor.execute("INSERT INTO ques VALUES (?,?,?,?,?,?,?,?)", data)
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


def get_all_questions():
    '''

    Returns: all questions from db

    '''
    cursor.execute("SELECT * FROM ques")
    fet = cursor.fetchall()
    return fet


def get_all_result():
    cursor.execute("SELECT * from results")
    fet = cursor.fetchall()
    return fet


def get_result_by_parent(parent):
    cursor.execute("SELECT results.* FROM results,users WHERE users.parent =? AND users.userName = results.kidName",
                   (parent,))
    fet = cursor.fetchall()
    return fet


def stampToTime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)


def timeToStamp(time):
    return datetime.datetime.timestamp(time)

def stampToStr(timestamp):
    time = stampToTime(timestamp)
    result = time.strftime("%d/%m/%y %H:%M")
    return result

def get_norm_time_now():
    '''

    Returns: time and date of now after normalize in STR format

    '''
    now_time = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
    #print(now_time)
    return now_time


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
        return fet[0]  # fetchone return tuple
    else:
        return


def get_game_number(kidName):
    cursor.execute("SELECT MAX(GameNumber) FROM results WHERE kidName=?", (kidName,))
    fet = cursor.fetchone()[0]
    if fet is None:
        return 0
    # print("number" ,fet)
    return fet


def get_next_game_number(kidName):
    return get_game_number(kidName) + 1


def get_next_qestion_id():
    '''

    Returns: id for next questions

    '''
    cursor.execute("SELECT max(qid) FROM ques")
    fet = cursor.fetchone()[0]
    # print(fet)
    if fet is not None:
        return fet + 1
    else:
        # init the first question
        return 1


def get_question_for_game(number_of_question):
    '''

    Args:
        number_of_question: number of questions

    Returns: list of questions

    '''
    if number_of_question == 0: return None
    # print("get_question_for_game:")
    if number_of_question > get_next_qestion_id() - 1:
        # תיקון מספר השאלות
        print("number of question modify to max ques in DB")
        number_of_question = get_next_qestion_id() - 1
    # set the questions to list
    cursor.execute("SELECT * FROM ques")
    ques_list = cursor.fetchall()
    # print("ques_list: ",len(ques_list))
    qList = []
    num_list = generate_rand_number_list(number_of_question)
    # print("num_list", num_list)
    for i in num_list:
        qList.append(ques_list[i - 1])
    return qList


def generate_rand_number_list(size):
    '''

    Args:
        size: int size of list

    Returns: list of random number for qid

    '''
    num_list = []
    for i in range(size):
        number = random.randint(1, size + 1)
        while number in num_list:
            number = random.randint(1, size + 1)
        num_list.append(number)
    return num_list


def check_answer(qid, ans):
    '''

    Args:
        qid: int number of question
        ans: player answer

    Returns: True if ans correct
             False if ans wrong

    '''
    cursor.execute("SELECT * FROM ques WHERE qid=?", (qid,))
    fet = cursor.fetchone()
    if fet is not None:
        true_ans = fet[7]  # return integer
        return true_ans == ans


def calc_game_success(kidName, gameNumber):
    '''

    Args:
        kidName: str of kid
        gameNumber: int of game

    Returns: game success rate

    '''
    correct_ans = 0
    param = (kidName, gameNumber)
    cursor.execute("SELECT * FROM gameLog WHERE kidName=? AND gameNumber = ?", param)
    fet = cursor.fetchall()
    for data in fet:
        if check_answer(data[2], data[3]):  # (qid,ans_to_check)
            # print(data)
            correct_ans += 1
    success_rate = correct_ans / len(fet)
    return success_rate


def export_table_to_csv(table_name):
    '''

    Args:
        table_name: str of table name

    Returns: export table to csv

    '''
    db_df = pd.read_sql_query("SELECT * FROM " + table_name, conn)
    file_name = table_name + ".csv"
    db_df.to_csv(file_name, index=False)
    print("table", table_name, "has been exported")

def export_result_by_parent(parent):
    '''

    Args:
        parent: str of parent

    Returns: export parents kid result to csv

    '''
    cursor.execute("SELECT * from results")
    names = list(map(lambda x: x[0], cursor.description))
    cursor.execute("SELECT results.* from results,users WHERE results.KidName = users.userName AND users.parent =?",(parent,))
    fet = cursor.fetchall()
    df = pd.DataFrame(fet, columns=names)
    print(df)
    path = parent+"_results.csv"
    df.to_csv(path)
    print("result for kids of",parent,"exported to file")


#export_result_by_parent("yaron")
#print(get_norm_time_now())