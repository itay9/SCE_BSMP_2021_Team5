import sqlite3

conn = sqlite3.connect("usersDB.db")
cursor = conn.cursor()

def login(user,password):
    """
    Args:
        user: string
        password: string

    Returns: user if login ok
            error message user or pass

    """
    cursor.execute("SELECT * FROM users WHERE userName = '"+user+"'")
    fet = cursor.fetchone()
    if fet is None:
        print("user does not exist!")
        return "wrong user"
    else:
        if fet[1] == password:
            print("login succss!")
            return fet[0] #return user name
        else:
            print("wrong password!")
            return "Wrong password"

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
        cursor.execute("INSERT INTO users VALUES ('"+user+"','"+password+"','parent','None')")
        print("register parent complete!")
        return True
    else:
        print("user already exist!, select different user name!")
        return False

def register_kid(user,password,parent):
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
        cursor.execute("INSERT INTO users VALUES ('"+user+"','"+password+"','kid','"+parent+"')")
        print("register kid complete!")
        return True
    else:
        print("user already exist!, select different user name!")
        return False

def register_admin(user,password):
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
        cursor.execute("INSERT INTO users VALUES ('"+user+"','"+password+"','admin','None')")
        print("register admin complete!")
        return True
    else:
        print("user already exist!, select different user name!")
        return False

def get_kids(parent):
    cursor.execute("SELECT * FROM users WHERE parent = '" + parent + "'")
    fet = cursor.fetchall()
    if len(fet)==0:
        print(parent,"has no kids in the system!")
    else:
        for kid in fet:
            print(kid[0])


#test
"""
login("itay","123") #ok
login("yaron","11234") #wrong pass
login("aa","aaa") #wrong user
"""
get_kids("yaron")
