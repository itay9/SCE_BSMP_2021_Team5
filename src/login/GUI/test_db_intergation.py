import sqlite3
import unittest
import DB
import os.path

class TestDb(unittest.TestCase):


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "usersDB.db")
    with sqlite3.connect(db_path) as conn:

    # with sqlite3.connect("usersDB.db") as conn:
        cursor = conn.cursor()

    @classmethod
    def setUpClass(cls):
        cls.cursor.execute("INSERT INTO users VALUES ('adminTest','123','admin','',1)")
        cls.cursor.execute("INSERT INTO users VALUES ('parentTest','123','parent','',1)")
        cls.cursor.execute("INSERT INTO users VALUES ('kidTest','123','kid','parentTest',0)")
        cls.conn.commit()
        print("setUp complete")

    @classmethod
    def tearDownClass(cls):
        cls.cursor.execute("DELETE FROM users WHERE userName= 'adminTest'")
        cls.cursor.execute("DELETE FROM users WHERE userName= 'parentTest'")
        cls.cursor.execute("DELETE FROM users WHERE userName= 'kidTest'")
        cls.conn.commit()
        print("tearDown complete")

    # def setUp(self):
    #     print('setUp')

    # def tearDown(self):
    #     print('tearDown\n')
    def test_check(self):
        self.assertEqual(True,True)

    def test_add_remove_user(self):
        self.cursor.execute("INSERT INTO users VALUES ('userTest',123,'kid','parentTest',0)")
        self.conn.commit()

        self.cursor.execute("SELECT * FROM users WHERE userName = 'userTest'")
        fet = self.cursor.fetchone()
        self.assertIsNotNone(fet)  # Test

        self.cursor.execute("SELECT * FROM users WHERE userName = ''")
        fet = self.cursor.fetchone()
        self.assertIsNone(fet)  # Test

        self.cursor.execute("DELETE FROM users WHERE userName= 'userTest'")
        self.conn.commit()

        # self.cursor.execute("SELECT * FROM users WHERE userName = 'tempUser'")
        # fet = self.cursor.fetchone()
        # self.assertIsNone(fet)  # Test

    def test_login_func(self):
        # cls.cursor.execute("INSERT INTO users VALUES ('adminTest','123','admin','')")#,1)")
        res = DB.login('adminTest', '123')
        self.assertEqual(res.lower(), "adminTest".lower())  # Test

        res = DB.login('adminTest', '')
        self.assertNotEqual(res.lower(), "adminTest".lower())  # Test

        res = DB.login('', '123')
        self.assertNotEqual(res.lower(), "adminTest".lower())  # Test

    def test_register_parent_func(self):
        # cls.cursor.execute("INSERT INTO users VALUES ('parentTest','123','parent','')")  # ,1)")
        res = DB.register_parent('parentTest', '123')
        self.assertNotEqual(res, True)  # Test

        # res=DB.register_parent('parentTest2','123')
        # self.assertEqual(res,True)#Test

        self.cursor.execute("DELETE FROM users WHERE userName= 'parentTest2'")
        self.conn.commit()

        # self.cursor.execute("SELECT * FROM users WHERE userName = 'parentTest2'")
        # fet = self.cursor.fetchone()
        # self.assertIsNone(fet)  # Test

    def test_register_kid_func(self):
        # cls.cursor.execute("INSERT INTO users VALUES ('parentTest','123','parent','')")  # ,1)")
        # res = DB.register_kid('kidTest', '123', '')
        # self.assertNotEqual(res, True)  # Test

        # res = DB.register_kid('kidTest', '123', 'parentTest')
        # self.assertNotEqual(res, True)  # Test

        res = DB.register_kid('kidTest2', '123', 'parentTest')
        self.assertEqual(res, True)  # Test

        self.cursor.execute("DELETE FROM users WHERE userName= 'kidTest2'")
        self.conn.commit()

        # self.cursor.execute("SELECT * FROM users WHERE userName = 'kidTest2'")
        # fet = self.cursor.fetchone()
        # self.assertIsNone(fet)  # Test

    def test_register_admin_func(self):
        # self.cursor.execute("INSERT INTO users VALUES ('parentTest','123','parent','',1)")
        res = DB.register_admin('adminTest', '123')
        self.assertNotEqual(res, True)  # Test

        # res=DB.register_admin('adminTest2','123')
        # self.assertEqual(res,True)#Test
        #
        # self.cursor.execute("DELETE FROM users WHERE userName= 'adminTest2'")
        # self.conn.commit()

        # self.cursor.execute("SELECT * FROM users WHERE userName = 'adminTest2'")
        # fet = self.cursor.fetchone()
        # self.assertIsNone(fet)  # Test

    def test_get_kids_func(self):
        # res = DB.get_kids('parentTest')
        # self.assertNotEqual(res,None)

        res = DB.get_kids(' ')
        self.assertIsNone(res)

        res = DB.get_kids('adminTest')
        self.assertIsNone(res)

    def test_remove_user_func(self):
        res = DB.remove_user('')
        self.assertNotEqual(res, True)#Test

        res = DB.remove_user('kidTest')
        self.assertEqual(res, True)#Test
        self.assertIsNone(DB.get_kids('parentTest'))#Test
        self.cursor.execute("INSERT INTO users VALUES ('kidTest','123','kid','parentTest',0)")
        self.conn.commit()

        res = DB.remove_user('parentTest')
        self.assertEqual(res, True)#Test

        self.cursor.execute("SELECT * FROM users WHERE userName = 'parentTest'")
        fet = self.cursor.fetchone()
        self.assertIsNone(fet)#Test

        self.cursor.execute("SELECT * FROM users WHERE userName = 'kidTest'")
        fet = self.cursor.fetchone()
        self.assertIsNone(fet)#Test

        self.cursor.execute("INSERT INTO users VALUES ('parentTest','123','parent','',1)")
        self.cursor.execute("INSERT INTO users VALUES ('kidTest','123','kid','parentTest',0)")
        self.conn.commit()




if __name__ == '__main__':
    unittest.main()
