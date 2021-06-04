import time
import pyttsx3
import DB

from PyQt5 import QtCore, QtGui, QtWidgets

NUM_OF_LEVELS = 2


class Ui_game_level(object):
    pushed = False
    last_game = False
    finish = False
    qid = -99999
    kidName = "test"
    correct_ans = 0
    current_level = 0
    number_of_games = -8888
    choice1 = "1"
    choice2 = "2"
    choice3 = "3"
    choice4 = "4"
    current_game = -77777
    global game_level

    def setupUi(self, game_level):
        game_level.setObjectName("game_level")
        game_level.resize(949, 691)
        self.centralwidget = QtWidgets.QWidget(game_level)
        self.centralwidget.setObjectName("centralwidget")
        self.image_game = QtWidgets.QLabel(self.centralwidget)
        self.image_game.setGeometry(QtCore.QRect(150, 120, 631, 271))
        self.image_game.setStyleSheet("background-image: url(:/newPrefix/‏‏לכידה.PNG);")
        self.image_game.setText("")
        self.image_game.setTextFormat(QtCore.Qt.AutoText)
        self.image_game.setPixmap(QtGui.QPixmap(":/newPrefix/‏‏לכידה.PNG"))
        self.image_game.setScaledContents(True)
        self.image_game.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.image_game.setObjectName("image_game")
        self.ans1_button = QtWidgets.QPushButton(self.centralwidget)
        self.ans1_button.setGeometry(QtCore.QRect(40, 450, 181, 81))
        self.ans1_button.setObjectName("ans1_button")
        self.ans2_button = QtWidgets.QPushButton(self.centralwidget)
        self.ans2_button.setGeometry(QtCore.QRect(280, 450, 181, 81))
        self.ans2_button.setObjectName("ans2_button")
        self.ans3_button = QtWidgets.QPushButton(self.centralwidget)
        self.ans3_button.setGeometry(QtCore.QRect(510, 450, 181, 81))
        self.ans3_button.setObjectName("ans3_button")
        self.ans4_button = QtWidgets.QPushButton(self.centralwidget)
        self.ans4_button.setGeometry(QtCore.QRect(740, 450, 181, 81))
        self.ans4_button.setObjectName("ans4_button")
        self.voice1_button = QtWidgets.QPushButton(self.centralwidget)
        self.voice1_button.setGeometry(QtCore.QRect(70, 580, 121, 51))
        self.voice1_button.setObjectName("voice1_button")
        self.voice4_button = QtWidgets.QPushButton(self.centralwidget)
        self.voice4_button.setGeometry(QtCore.QRect(770, 580, 121, 51))
        self.voice4_button.setObjectName("voice4_button")
        self.voice2_button = QtWidgets.QPushButton(self.centralwidget)
        self.voice2_button.setGeometry(QtCore.QRect(310, 580, 121, 51))
        self.voice2_button.setObjectName("voice2_button")
        self.voice3_button = QtWidgets.QPushButton(self.centralwidget)
        self.voice3_button.setGeometry(QtCore.QRect(540, 580, 121, 51))
        self.voice3_button.setObjectName("voice3_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(410, 30, 121, 51))
        self.exit_button.setObjectName("exit")
        self.qid_label = QtWidgets.QLabel(self.centralwidget)
        self.qid_label.setGeometry(QtCore.QRect(0, 0, 151, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.qid_label.setFont(font)
        self.qid_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.qid_label.setAlignment(QtCore.Qt.AlignCenter)
        self.qid_label.setObjectName("qid_label")
        self.score_label = QtWidgets.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(810, 20, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.score_label.setFont(font)
        self.score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.score_label.setObjectName("score_label")
        game_level.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(game_level)
        self.statusbar.setObjectName("statusbar")
        game_level.setStatusBar(self.statusbar)
        # bttn
        self.ans1_button.clicked.connect(self.click_ans1)
        self.ans2_button.clicked.connect(self.click_ans2)
        self.ans3_button.clicked.connect(self.click_ans3)
        self.ans4_button.clicked.connect(self.click_ans4)
        self.voice1_button.clicked.connect(self.click_hint1)
        self.voice2_button.clicked.connect(self.click_hint2)
        self.voice3_button.clicked.connect(self.click_hint3)
        self.voice4_button.clicked.connect(self.click_hint4)
        self.retranslateUi(game_level)
        QtCore.QMetaObject.connectSlotsByName(game_level)
        game_level.close()
        # @staticmethod
        # def close_this_game(game_level):
        #     game_level.close()

    def retranslateUi(self, game_level):
        _translate = QtCore.QCoreApplication.translate
        game_level.setWindowTitle(_translate("game_level", "MainWindow"))
        self.ans1_button.setText(_translate("game_level", "ans1"))
        self.ans2_button.setText(_translate("game_level", "ans2"))
        self.ans3_button.setText(_translate("game_level", "ans3"))
        self.ans4_button.setText(_translate("game_level", "ans4"))
        self.voice1_button.setText(_translate("game_level", "השמע"))
        self.voice4_button.setText(_translate("game_level", "השמע"))
        self.voice2_button.setText(_translate("game_level", "השמע"))
        self.voice3_button.setText(_translate("game_level", "השמע"))
        self.qid_label.setText(_translate("game_level", "00"))
        self.score_label.setText(_translate("game_level", "score"))
        self.exit_button.setText(_translate("game_level", "EXIT"))

    def set_new_game(self, new_game):
        '''
        
        Args:
            new_game: game row from DB

        Returns: update screen to new game

        '''

        if type(new_game) == list:
            new_game = new_game[0]
        self.qid = new_game[0]
        img_url = new_game[2]
        self.set_choice1(new_game[3])
        self.set_choice2(new_game[4])
        self.set_choice3(new_game[5])
        self.set_choice4(new_game[6])
        self.ans = new_game[7]
        self.set_ans1_bttn(self.choice1)
        self.set_ans2_bttn(self.choice2)
        self.set_ans3_bttn(self.choice3)
        self.set_ans4_bttn(self.choice4)
        self.set_img(img_url)
        self.pushed = False
        self.inc_current_level()
        self.set_qid_label()
        self.set_score_label()
        self.set_kid_name(DB.currentUser)
        self.set_current_game()
        if self.last_game:
            self.exit_button.setVisible(True)
        else:
            self.exit_button.setVisible(False)

    def set_finished(self):
        self.exit_button.setVisible(True)
        self.ans1_button.setVisible(False)
        self.ans2_button.setVisible(False)
        self.ans3_button.setVisible(False)
        self.ans4_button.setVisible(False)
        self.voice1_button.setVisible(False)
        self.voice2_button.setVisible(False)
        self.voice3_button.setVisible(False)
        self.voice4_button.setVisible(False)
        self.set_score_label()
        byeUrl = "pic/goodbye.jpg"
        self.set_img(byeUrl)


    def set_img(self, url):
        '''
        
        Args:
            url: url link from DB 

        Returns:

        '''
        self.image_game.setStyleSheet("background-image: url(" + url + ");")
        self.image_game.setPixmap(QtGui.QPixmap(url))

    def set_ans1_bttn(self, ans):
        self.ans1_button.setText(QtCore.QCoreApplication.translate("game_level", str(ans)))

    def set_ans2_bttn(self, ans):
        self.ans2_button.setText(QtCore.QCoreApplication.translate("game_level", str(ans)))

    def set_ans3_bttn(self, ans):
        self.ans3_button.setText(QtCore.QCoreApplication.translate("game_level", str(ans)))

    def set_ans4_bttn(self, ans):
        self.ans4_button.setText(QtCore.QCoreApplication.translate("game_level", str(ans)))

    def set_choice1(self, text):
        self.choice1 = text

    def set_choice2(self, text):
        self.choice2 = text

    def set_choice3(self, text):
        self.choice3 = text

    def set_choice4(self, text):
        self.choice4 = text

    def set_kid_name(self, name):
        self.kidName = name

    def set_current_game(self):
        current_game_ = DB.get_next_game_number(self.kidName)
        self.current_game = current_game_

    def set_number_of_games(self, num):
        self.number_of_games = num

    def set_score_label(self):
        self.score_label.setText(QtCore.QCoreApplication.translate("game_level", "Score: " + str(self.correct_ans)))

    def set_qid_label(self):
        self.qid_label.setText(QtCore.QCoreApplication.translate("game_level", "Question #" + str(self.qid)))

    def set_last_game(self):
        self.last_game = True
        print("last game")

    def click_ans1(self):
        self.recored_gameLog(self.qid, 1)
        if DB.check_answer(self.qid, 1):
            self.inc_correct_ans()
        self.pushed = True
        self.check_if_finish()

    def click_ans2(self):
        self.recored_gameLog(self.qid, 2)
        if DB.check_answer(self.qid, 2):
            self.inc_correct_ans()
        self.pushed = True
        self.check_if_finish()

    def click_ans3(self):
        self.recored_gameLog(self.qid, 3)
        if DB.check_answer(self.qid, 3):
            self.inc_correct_ans()
        self.pushed = True
        self.check_if_finish()

    def click_ans4(self):
        self.recored_gameLog(self.qid, 4)
        if DB.check_answer(self.qid, 4):
            self.inc_correct_ans()
        self.pushed = True
        self.check_if_finish()

    def click_hint1(self):
        self.play_hint(self.choice1)

    def click_hint2(self):
        self.play_hint(self.choice2)

    def click_hint3(self):
        self.play_hint(self.choice3)

    def click_hint4(self):
        self.play_hint(self.choice4)

    def wait_until_clicked(self):
        while self.pushed == False:
            QtCore.QCoreApplication.processEvents()

    def inc_correct_ans(self):
        self.correct_ans += 1

    def inc_current_level(self):
        self.current_level += 1

    def check_if_finish(self):
        if self.last_game == True:
            print("end game")
            # TODO maybe bug

    def play_hint(self, str_to_play):
        '''

        Args:
            str_to_play: string

        Returns: plays the hint

        '''
        engine = pyttsx3.init()
        engine.say(str_to_play)
        engine.runAndWait()

    def recored_gameLog(self, qid, ans):
        DB.add_result_to_gameLog(self.kidName, self.current_game, qid, ans)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    game_level = QtWidgets.QMainWindow()
    ui = Ui_game_level()
    ui.setupUi(game_level)
    """game_data = DB.get_question_for_game(NUM_OF_LEVELS)
    ui.set_number_of_games(len(game_data))
    player = DB.currentUser
    ui.set_kid_name(player)
    current_game = DB.get_game_number(player)
    ui.set_current_game(current_game)
    for data in game_data:
        ui.set_new_game(data)
        game_level.show()
        ui.wait_until_clicked()"""
    game_level.show()
    # print("correct ans:", ui.correct_ans)
    sys.exit(app.exec_())
