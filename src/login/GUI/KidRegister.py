from PyQt5 import QtCore, QtGui, QtWidgets
from src.login.GUI import DB

class Ui_kidRegister(object):
    def setupUi(self, kidRegister):
        kidRegister.setObjectName("kidRegister")
        kidRegister.resize(659, 400)
        kidRegister.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(kidRegister)
        self.centralwidget.setObjectName("centralwidget")
        self.ChildRegister = QtWidgets.QLabel(self.centralwidget)
        self.ChildRegister.setGeometry(QtCore.QRect(20, -70, 661, 271))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.ChildRegister.setFont(font)
        self.ChildRegister.setObjectName("ChildRegister")
        self.userName_input = QtWidgets.QLineEdit(self.centralwidget)
        self.userName_input.setGeometry(QtCore.QRect(70, 160, 201, 41))
        self.userName_input.setObjectName("userName_input")
        self.PW_input = QtWidgets.QLineEdit(self.centralwidget)
        self.PW_input.setGeometry(QtCore.QRect(70, 240, 201, 41))
        self.PW_input.setInputMask("")
        self.PW_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PW_input.setObjectName("PW_input")
        self.PW_label = QtWidgets.QLabel(self.centralwidget)
        self.PW_label.setGeometry(QtCore.QRect(70, 220, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PW_label.setFont(font)
        self.PW_label.setObjectName("PW_label")
        self.UName_label = QtWidgets.QLabel(self.centralwidget)
        self.UName_label.setGeometry(QtCore.QRect(70, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UName_label.setFont(font)
        self.UName_label.setObjectName("UName_label")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(340, 310, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.registerButton.setFont(font)
        self.registerButton.setObjectName("registerButton")
        self.exit_Bttn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_Bttn.setGeometry(QtCore.QRect(500, 310, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit_Bttn.setFont(font)
        self.exit_Bttn.setObjectName("exit_Bttn")
        kidRegister.setCentralWidget(self.centralwidget)

        #button func
        self.registerButton.clicked.connect(self.regClick)
        self.exit_Bttn.clicked.connect(self.mainMenu_UI)
        self.exit_Bttn.clicked.connect(kidRegister.close)
        self.exit_Bttn.clicked.connect(DB.logOut)
        
        
        self.retranslateUi(kidRegister)
        QtCore.QMetaObject.connectSlotsByName(kidRegister)

    def regClick(self):
        if DB.sassionFlag == True:
            user = self.userName_input.text()
            if DB.canRegister(user):
                pw = self.PW_input.text()
                parent = DB.currentUser
                DB.register_kid(user,pw,parent)

    def retranslateUi(self, kidRegister):
        _translate = QtCore.QCoreApplication.translate
        kidRegister.setWindowTitle(_translate("kidRegister", "MainWindow"))
        self.ChildRegister.setText(_translate("kidRegister", "Child Register"))
        self.PW_label.setText(_translate("kidRegister", "Password:"))
        self.UName_label.setText(_translate("kidRegister", "Username:"))
        self.registerButton.setText(_translate("kidRegister", "Register"))
        self.exit_Bttn.setText(_translate("kidRegister", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kidRegister = QtWidgets.QMainWindow()
    ui = Ui_kidRegister()
    ui.setupUi(kidRegister)
    kidRegister.show()
    sys.exit(app.exec_())
