import sqlite3

conn = sqlite3.connect("usersDB.db")
cursor = conn.cursor()

currentUser = ""
sassionFlag = False


# DB init table
def db_init():
    cursor.execute("""CREATE TABLE users
                (userName text,
                pass text,
                type text, 
                parent text,
                canReg integer)""")  # type is admin , parent or kid
    # db insert rows
    cursor.execute("INSERT INTO users VALUES ('itay','123','admin','',1)")
    cursor.execute("INSERT INTO users VALUES ('yaron','123','parent','',1)")
    cursor.execute("INSERT INTO users VALUES ('chen','123','kid','yaron',0)")
    cursor.execute("INSERT INTO users VALUES ('yaniv','123','kid','yaron',0)")
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
    cursor.execute("SELECT * FROM users WHERE userName = '" + user + "'")
    fet = cursor.fetchone()
    if fet is None:
        cursor.execute("INSERT INTO users VALUES ('" + user + "','" + password + "','parent','None',0)")
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
    cursor.execute("SELECT * FROM users WHERE userName = '" + user + "'")
    fet = cursor.fetchone()
    if fet is None:
        cursor.execute("INSERT INTO users VALUES ('" + user + "','" + password + "','kid','" + parent + "',0)")
        conn.commit()
        print("register kid complete!")
        return True
    else:
        print("user already exist!, select different user name!")
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
        cursor.execute("INSERT INTO users VALUES ('" + user + "','" + password + "','admin','None',1)") #new
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
    cursor.execute("SELECT * FROM users WHERE parent='" + parent + "'")
    fet = cursor.fetchall()
    if len(fet) == 0:
        print(parent, "has no kids in the system!")
        return []
    else:
        kids_list = []
        for kid in fet:
            kids_list.append(kid[0])
        print(kids_list)
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
    if fet[2] == "parent":
        for kid in get_kids(user):
            remove_user(kid)
    cursor.execute("DELETE FROM users WHERE userName= '" + user + "'")
    conn.commit()
    print(user,"removed")
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

"""
def allowReg(parent):
    cursor.execute(UPDATE usersDB
    SET
    canReg = 1,
    WHERE
    userName=''
"""
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
"""