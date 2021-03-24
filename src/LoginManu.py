import sqlite3

conn = sqlite3.connect("usersDB.db")
cursor = conn.cursor()

def login(user,password):
    """

    Args:
        user:
        password:

    Returns:

    """
    cursor.execute("SELECT * FROM users WHERE userName = '"+user+"'")
    fet = cursor.fetchone()
    if fet is None:
        print("user does not exist!")
        return False
    else:
        if fet[1] == password:
            print("login succss!")
            return True
        else:
            print("wrong password!")
            return False

def register_parent(user,password):
    """

    Args:
        user: string
        password: string

    Returns: register parent to DB

    """
    cursor.execute("SELECT * FROM users WHERE userName = '" + user + "'")
    fet = cursor.fetchone()
    if fet is None:
        cursor.execute("INSERT INTO users VALUES ('"+user+"','"+password+"','parent')")
        print("register parent complete!")
    else:
        print("user already exist!, select different user name!")

def register_kid(user,password,parent):
    """

    Args:
        user: name of the kid
        password:
        parent: name of parent

    Returns: register new kid to DB

    """
    cursor.execute("SELECT * FROM users WHERE userName = '" + user + "'")
    fet = cursor.fetchone()
    if fet is None:
        cursor.execute("INSERT INTO users VALUES ('"+user+"','"+password+"','kid')")
        print("register kid complete!")
    else:
        print("user already exist!, select different user name!")

def get_kids(parent):

    pass
#test
"""
login("itay","123") #ok
login("yaron","11234") #wrong pass
login("aa","aaa") #wrong user
"""