import sqlite3
import gameDB
conn = sqlite3.connect("GameDB.db")
cursor = conn.cursor()

currentUser = "defult"
sassionFlag = False


# DB init table
def db_init():
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
    if par_reg==0:
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

#get data funcs
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
        cursor.execute("SELECT * FROM users WHERE parent=?",(parent,))
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
    if kid_allow==0:
        cursor.execute("UPDATE users SET canPlay = 1 WHERE userName= ? ", (kid,))
    else:
        cursor.execute("UPDATE users SET canPlay = 0 WHERE userName= ? ", (kid,))
    conn.commit()


# test
"""
login("itay","123") #ok
login("yaron","11234") #wrong pass
login("aa","aaa") #wrong user
get_kids("yaron")

register_parent("a", "123")
register_kid("b", "123", "a")
register_kid("c", "123", "a")
get_kids("a")
login("a", "123")
login("b", "123")
login("c", "123")
remove_user("a")
login("a", "123")
login("b", "123")
login("c", "123")
remove_user("a")
register_parent("a","a")
register_kid("b","b","a")
allowReg("a")
register_kid("b","b","a")
"""

def build_db():
    try:
        db_init()
        gameDB.init_QDB()
        gameDB.init_kidDB()
        gameDB.init_game_log_DB()
    except:
        pass

