from PyQt5 import QtCore, QtGui, QtWidgets
import DB
import MainMenu
import game_gui
NUM_OF_GAME = 2

class Ui_kidMenu(object):
    def setupUi(self, kidMenu):
        kidMenu.setObjectName("kidMenu")
        kidMenu.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(kidMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.StartNewGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartNewGameButton.setGeometry(QtCore.QRect(260, 260, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.StartNewGameButton.setFont(font)
        self.StartNewGameButton.setObjectName("StartNewGameButton")
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QtCore.QRect(580, 480, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(160, 70, 481, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        kidMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(kidMenu)
        self.statusbar.setObjectName("statusbar")
        kidMenu.setStatusBar(self.statusbar)

        #bttn connect:
        self.logoutButton.clicked.connect(DB.logOut)
        self.logoutButton.clicked.connect(self.mainMenu_UI)
        self.logoutButton.clicked.connect(kidMenu.close)
        self.StartNewGameButton.clicked.connect(self.newGame)

        self.retranslateUi(kidMenu)
        QtCore.QMetaObject.connectSlotsByName(kidMenu)

    def mainMenu_UI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MainMenu.Ui_mainMenu()
        self.ui.setupUi(self.window)
        self.window.show()

    def newGame(self):
        game_data = DB.get_question_for_game(2) #TODO The problem starts from here.
        player = DB.currentUser
        self.window = QtWidgets.QMainWindow()
        self.ui = game_gui.Ui_game_level()
        self.ui.setupUi(self.window)
        self.window.show()
        for index in range(len(game_data)):
            data = game_data[index]
            self.ui.set_new_game(data)
            self.window.show()
            self.ui.wait_until_clicked()
        self.ui.set_finished()
        self.window.show()


        print("game finish")
        DB.add_result_to_Kidsdb(player)





    def retranslateUi(self, kidMenu):
        _translate = QtCore.QCoreApplication.translate
        kidMenu.setWindowTitle(_translate("kidMenu", "MainWindow"))
        self.StartNewGameButton.setText(_translate("kidMenu", "Start New Game"))
        self.logoutButton.setText(_translate("kidMenu", "Log Out"))
        self.title.setText(_translate("kidMenu", "Kids Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kidMenu = QtWidgets.QMainWindow()
    ui = Ui_kidMenu()
    ui.setupUi(kidMenu)
    kidMenu.show()
    sys.exit(app.exec_())
