from PyQt5 import QtCore, QtGui, QtWidgets
import Success_POP
import MainMenu
import DB


class Ui_parentRegister(object):

    def Success_UI(self):
        self.window = QtWidgets.QWidget()
        self.ui = Success_POP.Ui_Parent_Registered()
        self.ui.setupUi(self.window)
        self.window.show()

    def return_mainMneu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MainMenu.Ui_mainMenu()
        self.ui.setupUi(self.window)
        self.window.show()

    def register_parent(self):
        user = self.userNameInput.text()
        pw = self.pwInput.text()
        DB.register_parent(user, pw)

    def setupUi(self, parentRegister):
        parentRegister.setObjectName("parentRegister")
        parentRegister.resize(795, 506)
        self.centralwidget = QtWidgets.QWidget(parentRegister)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(40, 60, 731, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.passLabel = QtWidgets.QLabel(self.centralwidget)
        self.passLabel.setGeometry(QtCore.QRect(30, 250, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.passLabel.setFont(font)
        self.passLabel.setObjectName("passLabel")
        self.pwInput = QtWidgets.QLineEdit(self.centralwidget)
        self.pwInput.setGeometry(QtCore.QRect(170, 250, 251, 31))
        self.pwInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwInput.setObjectName("pwInput")
        self.userNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.userNameInput.setGeometry(QtCore.QRect(170, 190, 251, 31))
        self.userNameInput.setObjectName("userNameInput")
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(30, 190, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.userLabel.setFont(font)
        self.userLabel.setObjectName("userLabel")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(480, 340, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.registerButton.setFont(font)
        self.registerButton.setObjectName("registerButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(630, 340, 131, 41))

        # self.exitButton.clicked.connect(""" Make Function for returing to main""")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        parentRegister.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parentRegister)
        self.statusbar.setObjectName("statusbar")
        parentRegister.setStatusBar(self.statusbar)

        # bttn connect
        self.exitButton.clicked.connect(self.return_mainMneu)
        self.exitButton.clicked.connect(parentRegister.close)
        self.registerButton.clicked.connect(self.Success_UI)
        self.registerButton.clicked.connect(parentRegister.close)
        self.registerButton.clicked.connect(self.register_parent)
        
        self.retranslateUi(parentRegister)
        QtCore.QMetaObject.connectSlotsByName(parentRegister)

    def retranslateUi(self, parentRegister):
        _translate = QtCore.QCoreApplication.translate
        parentRegister.setWindowTitle(_translate("parentRegister", "MainWindow"))
        self.title.setText(_translate("parentRegister", "Parent Register Menu"))
        self.passLabel.setText(_translate("parentRegister", "Password:"))
        self.userLabel.setText(_translate("parentRegister", "User Name:"))
        self.registerButton.setText(_translate("parentRegister", "Register"))
        self.exitButton.setText(_translate("parentRegister", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    parentRegister = QtWidgets.QMainWindow()
    ui = Ui_parentRegister()
    ui.setupUi(parentRegister)
    parentRegister.show()
    sys.exit(app.exec_())
