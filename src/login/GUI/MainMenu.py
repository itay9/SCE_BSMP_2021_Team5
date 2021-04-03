
from PyQt5 import QtCore, QtGui, QtWidgets
from ParentRegister import Ui_parentRegister

from src.login.GUI import DB
class Ui_mainMenu(object):

    def openParentRegister(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_parentRegister()
        self.ui.setupUi(self.window)
        mainMenu.hide()
        self.window.show()


    def setupUi(self, mainMenu):
        mainMenu.setObjectName("mainMenu")
        mainMenu.resize(684, 463)
        self.centralwidget = QtWidgets.QWidget(mainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(100, 340, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.parentRegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.parentRegisterButton.setGeometry(QtCore.QRect(400, 340, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parentRegisterButton.setFont(font)
        self.parentRegisterButton.setObjectName("parentRegisterButton")
        self.parentRegisterButton.clicked.connect(self.openParentRegister)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, 20, 481, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(30, 200, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.userLabel.setFont(font)
        self.userLabel.setObjectName("userLabel")
        self.passLabel = QtWidgets.QLabel(self.centralwidget)
        self.passLabel.setGeometry(QtCore.QRect(30, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.passLabel.setFont(font)
        self.passLabel.setObjectName("passLabel")
        self.userNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.userNameInput.setGeometry(QtCore.QRect(170, 200, 251, 31))
        self.userNameInput.setObjectName("userNameInput")
        self.pwInput = QtWidgets.QLineEdit(self.centralwidget)
        self.pwInput.setGeometry(QtCore.QRect(170, 260, 251, 31))
        self.pwInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwInput.setObjectName("pwInput")
        mainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 26))
        self.menubar.setObjectName("menubar")
        mainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainMenu)
        self.statusbar.setObjectName("statusbar")
        mainMenu.setStatusBar(self.statusbar)
        #bttn func
        self.loginButton.clicked.connect(self.onClick)
        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def onClick(self):
        DB.login(self.userNameInput.text(),self.pwInput.text())
        nextWindow = DB.get_type(DB.currentUser)
        if nextWindow == "admin":
            pass
            #TODO open admin window
        elif nextWindow == "parent":
            pass
            #TODO open parent window
        elif nextWindow == "kid":
            pass
            #TODO open kid window

    def retranslateUi(self, mainMenu):
        _translate = QtCore.QCoreApplication.translate
        mainMenu.setWindowTitle(_translate("mainMenu", "MainWindow"))
        self.loginButton.setText(_translate("mainMenu", "Log In"))
        self.parentRegisterButton.setText(_translate("mainMenu", "Parent Register"))
        self.title.setText(_translate("mainMenu", "Welcome!"))
        self.userLabel.setText(_translate("mainMenu", "User Name:"))
        self.passLabel.setText(_translate("mainMenu", "Password:"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainMenu = QtWidgets.QMainWindow()
    ui = Ui_mainMenu()
    ui.setupUi(mainMenu)
    mainMenu.show()
    sys.exit(app.exec_())
