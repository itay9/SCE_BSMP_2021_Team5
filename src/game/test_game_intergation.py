import sqlite3
import unittest
import gameDB
import os.path


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
        print("setUp complete")

    @classmethod
    def tearDownClass(cls):
        cls.cursor.execute("DELETE FROM ques WHERE qid= 999")
        cls.cursor.execute("DELETE FROM ques WHERE qid= 9999")
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


if __name__ == '__main__':
    unittest.main()
