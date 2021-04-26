import time

from PyQt5 import QtCore, QtGui, QtWidgets
import gameDB
NUM_OF_LEVELS = 2

class Ui_game_level(object):
    pushed = False
    qid = -99999
    kidName = "test"
    correct_ans = 0
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
        #bttn
        self.ans1_button.clicked.connect(self.click_ans1)
        self.ans2_button.clicked.connect(self.click_ans2)
        self.ans3_button.clicked.connect(self.click_ans3)
        self.ans4_button.clicked.connect(self.click_ans4)
        self.retranslateUi(game_level)
        QtCore.QMetaObject.connectSlotsByName(game_level)

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
    def set_new_game(self,new_game):
        '''
        
        Args:
            new_game: game row from DB

        Returns: update screen to new game

        '''
        print(new_game)
        #global qid
        self.qid = new_game[0]
        img_url = new_game[2]
        choice1 = new_game[3]
        choice2 = new_game[4]
        choice3 = new_game[5]
        choice4 = new_game[6]
        self.ans = new_game[7]
        self.set_ans1_bttn(choice1)
        self.set_ans2_bttn(choice2)
        self.set_ans3_bttn(choice3)
        self.set_ans4_bttn(choice4)
        self.set_img(img_url)
        self.pushed = False

    def set_img(self,url):
        '''
        
        Args:
            url: url link from DB 

        Returns:

        '''
        self.image_game.setStyleSheet("background-image: url("+url+");")
        self.image_game.setPixmap(QtGui.QPixmap(url))
    
    def set_ans1_bttn(self,ans):
        self.ans1_button.setText(QtCore.QCoreApplication.translate("game_level", str(ans)))
    def set_ans2_bttn(self, ans):
        self.ans2_button.setText(QtCore.QCoreApplication.translate("game_level", str(ans)))
    def set_ans3_bttn(self, ans):
        self.ans3_button.setText(QtCore.QCoreApplication.translate("game_level", str(ans)))
    def set_ans4_bttn(self, ans):
        self.ans4_button.setText(QtCore.QCoreApplication.translate("game_level", str(ans)))
    def click_ans1(self):
        print(gameDB.check_answer(self.qid,1))
        if gameDB.check_answer(self.qid,1):
            self.inc_correct_ans()
        self.pushed = True
    def click_ans2(self):
        print(gameDB.check_answer(self.qid,2))
        if gameDB.check_answer(self.qid,2):
            self.inc_correct_ans()
        self.pushed = True
    def click_ans3(self):
        print(gameDB.check_answer(self.qid,3))
        if gameDB.check_answer(self.qid,3):
            self.inc_correct_ans()
        self.pushed = True
    def click_ans4(self):
        print(gameDB.check_answer(self.qid,4))
        if gameDB.check_answer(self.qid,4):
            self.inc_correct_ans()
        self.pushed = True
    def wait_until_clicked(self):
        while self.pushed==False:
            QtCore.QCoreApplication.processEvents()
    def inc_correct_ans(self):
        self.correct_ans+=1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game_level = QtWidgets.QMainWindow()
    ui = Ui_game_level()
    ui.setupUi(game_level)
    game_data = gameDB.get_question_for_game(3)
    for data in game_data:
        ui.set_new_game(data)
        game_level.show()
        ui.wait_until_clicked()
    print("correct ans:",ui.correct_ans)
    sys.exit(app.exec_())
