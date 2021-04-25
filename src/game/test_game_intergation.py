import sqlite3
import unittest
import gameDB
import os.path
from datetime import datetime


class GameTest(unittest.TestCase):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "gameDB.db")
    with sqlite3.connect(db_path) as conn:
        # with sqlite3.connect("usersDB.db") as conn:
        cursor = conn.cursor()

    @classmethod
    def setUpClass(cls):
        cls.cursor.execute("INSERT INTO ques VALUES (999,'firstQ','url','a','b','c','d',1)")
        cls.cursor.execute("INSERT INTO ques VALUES (9999,'secondQ','url','e','f','g','h',2)")
        cls.conn.commit()

        date = datetime.now()
        cls.cursor.execute("INSERT into results VALUES ('chenA', ?, 1, 2, 80)", (date,))
        cls.conn.commit()

        print("setUp complete")

    @classmethod
    def tearDownClass(cls):
        cls.cursor.execute("DELETE FROM ques WHERE qid= 999")
        cls.cursor.execute("DELETE FROM ques WHERE qid= 9999")
        cls.conn.commit()

        cls.cursor.execute("DELETE FROM results WHERE KidName= 'chenA'")
        cls.conn.commit()
        print("tearDown complete")
        cls.conn.close()

    def test_check(self):
        self.assertEqual(True, True)

    def test_get_ques(self):
        self.cursor.execute("SELECT qid FROM ques WHERE qid = 999")
        fet = self.cursor.fetchone()[0]  # first arg from fet(return tuple)
        self.assertEqual(fet, 999)

        res = gameDB.get_question_from_id(999)
        self.assertIsNotNone(res)
        print("question is:", res)

        res = gameDB.get_question_from_id(99999)
        self.assertIsNone(res)

    def test_add_ques(self):
        qst = ('testQ', 'url', 'a', 'b', 'c', 'd', 1)
        gameDB.add_question_to_qdb(*qst)

        self.cursor.execute("SELECT qid FROM ques WHERE quesion = 'testQ'")
        fet = self.cursor.fetchone()
        self.assertIsNotNone(fet)

        self.cursor.execute("DELETE FROM ques WHERE quesion = 'testQ'")
        self.conn.commit()

    def test_get_id(self):

        res=gameDB.get_qestion_id()
        self.assertEqual(res,1000)





    def test_get_ans(self):
        self.cursor.execute("SELECT answer FROM ques WHERE qid = 999")
        fet = self.cursor.fetchone()[0]
        self.assertEqual(fet, 1)

        res = gameDB.get_ans(999)
        self.assertEqual(res, 1)

        res = gameDB.get_ans(99999)
        self.assertIsNone(res)

    def test_kidsDB(self):
        self.cursor.execute("SELECT * FROM results")
        fet = self.cursor.fetchall()
        self.assertIsNotNone(fet)

        self.cursor.execute("SELECT * FROM results WHERE KidName = 'chenA'")
        fet = self.cursor.fetchone()
        self.assertIsNotNone(fet)

    def test_add_result(self):
        date = datetime.now()
        self.cursor.execute("INSERT into results VALUES ('chenB', ?, 1, 2, 80)", (date,))
        self.conn.commit()

        self.cursor.execute("SELECT * FROM results WHERE KidName = 'chenB'")
        fet = self.cursor.fetchone()
        self.assertIsNotNone(fet)

        self.cursor.execute("DELETE FROM results WHERE KidName= 'chenB'")
        self.conn.commit()

        tup = ('chenB', datetime.now(), 1, 100)
        gameDB.add_result_to_Kidsdb(*tup)

        self.cursor.execute("SELECT * FROM results WHERE KidName = 'chenB'")
        fet = self.cursor.fetchone()
        self.assertIsNotNone(fet)

        self.cursor.execute("DELETE FROM results WHERE KidName= 'chenB'")
        self.conn.commit()

    def test_get_kid_res(self):
        self.cursor.execute("SELECT * FROM results WHERE kidName =?", ('chenA',))
        fet = self.cursor.fetchall()
        self.assertIsNotNone(fet)

        res = gameDB.get_kid_results('chenA')
        self.assertIsNotNone(fet)

        res = gameDB.get_kid_results('chenABCD')
        self.assertIsNone(res)

        res = gameDB.get_kid_results('')
        self.assertIsNone(res)

    def test_get_game_number(self):
        self.cursor.execute("SELECT * FROM results WHERE kidName =?", ('chenA',))
        fet = self.cursor.fetchall()
        self.assertEqual(len(fet), 1)

        self.cursor.execute("SELECT * FROM results WHERE kidName =?", ('chenABCD',))
        fet = self.cursor.fetchone()
        self.assertIsNone(fet)

    def test_get_list_of_qeus(self):
        ques_list=[]
        ques_list=gameDB.get_question_for_game(2)
        self.assertEqual(len(ques_list),2)

        ques_list = gameDB.get_question_for_game(1)
        self.assertEqual(len(ques_list), 1)

        ques_list = gameDB.get_question_for_game(0)
        self.assertIsNone(ques_list)





if __name__ == '__main__':
    unittest.main()
