
from PyQt5 import QtCore, QtGui, QtWidgets
import ShowQuestions
import AllowParentReg
import AllowKidPlay
import MainMenu
import DB
import DeleteUser
class Ui_ManagerMenu(object):

    def setupUi(self, ManagerMenu):
        ManagerMenu.setObjectName("ManagerMenu")
        ManagerMenu.resize(828, 600)
        ManagerMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(ManagerMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOutButton.setGeometry(QtCore.QRect(50, 480, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.logOutButton.setFont(font)
        self.logOutButton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.logOutButton.setObjectName("logOutButton")
        self.viewChildResultButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewChildResultButton.setGeometry(QtCore.QRect(50, 230, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.viewChildResultButton.setFont(font)
        self.viewChildResultButton.setObjectName("viewChildResultButton")
        self.allowKidPlayButton = QtWidgets.QPushButton(self.centralwidget)
        self.allowKidPlayButton.setGeometry(QtCore.QRect(480, 230, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.allowKidPlayButton.setFont(font)
        self.allowKidPlayButton.setObjectName("allowKidPlayButton")
        self.viewQuestionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewQuestionsButton.setGeometry(QtCore.QRect(50, 350, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.viewQuestionsButton.setFont(font)
        self.viewQuestionsButton.setObjectName("viewQuestionsButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(130, 60, 601, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.deleteUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteUserButton.setGeometry(QtCore.QRect(480, 350, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.deleteUserButton.setFont(font)
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.allowParentRegButton = QtWidgets.QPushButton(self.centralwidget)
        self.allowParentRegButton.setGeometry(QtCore.QRect(480, 480, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.allowParentRegButton.setFont(font)
        self.allowParentRegButton.setObjectName("allowParentRegButton")
        ManagerMenu.setCentralWidget(self.centralwidget)

        #bttn connect
        self.logOutButton.clicked.connect(self.mainMenu_UI)
        self.logOutButton.clicked.connect(ManagerMenu.close)
        self.logOutButton.clicked.connect(DB.logOut)
        self.deleteUserButton.clicked.connect(self.open_deleteUser_UI)
        self.allowKidPlayButton.clicked.connect(self.open_AllowKidPlay_UI)
        self.allowParentRegButton.clicked.connect(self.open_AllowParenReg_UI)
        self.viewQuestionsButton.clicked.connect(self.open_ShowQuestions_UI)


        self.retranslateUi(ManagerMenu)
        QtCore.QMetaObject.connectSlotsByName(ManagerMenu)

    def retranslateUi(self, ManagerMenu):
        _translate = QtCore.QCoreApplication.translate
        ManagerMenu.setWindowTitle(_translate("ManagerMenu", "MainWindow"))
        self.logOutButton.setText(_translate("ManagerMenu", "Log Out"))
        self.allowKidPlayButton.setText(_translate("ManagerMenu", "Allow Kid to Play")) #
        self.viewChildResultButton.setText(_translate("ManagerMenu", "View Child result"))
        self.viewQuestionsButton.setText(_translate("ManagerMenu", "View Questions"))
        self.title.setText(_translate("ManagerMenu", "Maneger Menu"))
        self.deleteUserButton.setText(_translate("ManagerMenu", "Delete a User"))
        self.allowParentRegButton.setText(_translate("ManagerMenu", "Allow Parent Reg"))

    def mainMenu_UI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MainMenu.Ui_mainMenu()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_deleteUser_UI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = DeleteUser.Ui_DeleteUser()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_AllowKidPlay_UI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AllowKidPlay.Ui_AllowKidPlay()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_AllowParenReg_UI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AllowParentReg.Ui_AllowParentReg()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_ShowQuestions_UI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ShowQuestions.Ui_QuestionTable()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManagerMenu = QtWidgets.QMainWindow()
    ui = Ui_ManagerMenu()
    ui.setupUi(ManagerMenu)
    ManagerMenu.show()
    sys.exit(app.exec_())
