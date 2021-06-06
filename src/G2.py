from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_game_level(object):
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
        self.voice4_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.voice4_button_2.setGeometry(QtCore.QRect(410, 30, 121, 51))
        self.voice4_button_2.setObjectName("voice4_button_2")
        game_level.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(game_level)
        self.statusbar.setObjectName("statusbar")
        game_level.setStatusBar(self.statusbar)

        self.retranslateUi(game_level)
        QtCore.QMetaObject.connectSlotsByName(game_level)

    def retranslateUi(self, game_level):
        _translate = QtCore.QCoreApplication.translate
        game_level.setWindowTitle(_translate("game_level", "MainWindow"))
        self.ans1_button.setText(_translate("game_level", "ans1"))
        self.ans2_button.setText(_translate("game_level", "ans2"))
        self.ans3_button.setText(_translate("game_level", "ans3"))
        self.ans4_button.setText(_translate("game_level", "ans4"))
        self.voice1_button.setText(_translate("game_level", "voice1"))
        self.voice4_button.setText(_translate("game_level", "voice4"))
        self.voice2_button.setText(_translate("game_level", "voice2"))
        self.voice3_button.setText(_translate("game_level", "voice3"))
        self.qid_label.setText(_translate("game_level", "00"))
        self.score_label.setText(_translate("game_level", "score"))
        self.voice4_button_2.setText(_translate("game_level", "EXIT"))
#import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game_level = QtWidgets.QMainWindow()
    ui = Ui_game_level()
    ui.setupUi(game_level)
    game_level.show()
    sys.exit(app.exec_())