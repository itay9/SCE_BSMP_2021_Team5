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

    def test_check(self):
        self.assertEqual(True, True)

    def test_get_ques(self):
        self.cursor.execute("SELECT qid FROM ques WHERE qid = 999")
        fet = self.cursor.fetchone()[0]  # first arg from fet(return tuple)
        self.assertEqual(fet, 999)

        res = gameDB.get_question_from_id(999)
        print("question is:", res)


if __name__ == '__main__':
    unittest.main()
