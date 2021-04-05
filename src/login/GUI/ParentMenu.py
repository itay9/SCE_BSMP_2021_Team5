from PyQt5 import QtCore, QtGui, QtWidgets
import MainMenu
import deleteChild
import DB
import kidRegister

class Ui_parentMenu(object):

    def deleteThisUser(self):
        #TODO fix bug, prog crush after click DELETE THIS USER
        DB.remove_user(DB.currentUser)
        DB.logOut()
        self.mainMenu_UI()
        parentMenu.close()
        #need to fix BUG !
        ##
    def openChildDelete(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = deleteChild.Ui_ChildTableDelete()
        self.ui.setupUi(self.window)
        self.window.show()

    def mainMenu_UI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MainMenu.Ui_mainMenu()
        self.ui.setupUi(self.window)
        self.window.show()
       
    def register_kid(self):
        if DB.canRegister(DB.currentUser):
            self.window = QtWidgets.QMainWindow()
            self.ui = kidRegister.Ui_mainMenu()
            self.ui.setupUi(self.window)
            self.window.show()

    def setupUi(self, parentMenu):
        parentMenu.setObjectName("parentMenu")
        parentMenu.resize(795, 577)
        self.centralwidget = QtWidgets.QWidget(parentMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.ViewChildData = QtWidgets.QPushButton(self.centralwidget)
        self.ViewChildData.setGeometry(QtCore.QRect(510, 250, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ViewChildData.setFont(font)
        self.ViewChildData.setObjectName("ViewChildData")
        self.registerChild = QtWidgets.QPushButton(self.centralwidget)
        self.registerChild.setGeometry(QtCore.QRect(50, 250, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.registerChild.setFont(font)
        self.registerChild.setObjectName("registerChild")
        self.DeleteChild = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteChild.setGeometry(QtCore.QRect(50, 370, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteChild.setFont(font)
        self.DeleteChild.setObjectName("DeleteChild")
        self.DeleteParentUser = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteParentUser.setGeometry(QtCore.QRect(510, 380, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteParentUser.setFont(font)
        self.DeleteParentUser.setObjectName("DeleteParentUser")
        self.LogOut = QtWidgets.QPushButton(self.centralwidget)
        self.LogOut.setGeometry(QtCore.QRect(320, 480, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LogOut.setFont(font)
        self.LogOut.setObjectName("LogOut")
        self.ParentMenu = QtWidgets.QLabel(self.centralwidget)
        self.ParentMenu.setGeometry(QtCore.QRect(120, 10, 581, 141))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.ParentMenu.setFont(font)
        self.ParentMenu.setObjectName("ParentMenu")
        parentMenu.setCentralWidget(self.centralwidget)

        #bttn connect
        self.LogOut.clicked.connect(self.mainMenu_UI)
        self.LogOut.clicked.connect(parentMenu.close)
        self.LogOut.clicked.connect(DB.logOut)
        self.DeleteChild.clicked.connect(self.openChildDelete)
        self.DeleteChild.clicked.connect(parentMenu.close)
        self.DeleteParentUser.clicked.connect(self.deleteThisUser)

        self.retranslateUi(parentMenu)
        QtCore.QMetaObject.connectSlotsByName(parentMenu)

    def retranslateUi(self, parentMenu):
        _translate = QtCore.QCoreApplication.translate
        parentMenu.setWindowTitle(_translate("parentMenu", "Parent Menu"))
        self.ViewChildData.setText(_translate("parentMenu", "View Child Data"))
        self.registerChild.setText(_translate("parentMenu", "Register Child "))
        self.DeleteChild.setText(_translate("parentMenu", "Delete Child"))
        self.DeleteParentUser.setText(_translate("parentMenu", "Delete this user"))
        self.LogOut.setText(_translate("parentMenu", "Log Out"))
        self.ParentMenu.setText(_translate("parentMenu", "Parent Menu"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    parentMenu = QtWidgets.QMainWindow()
    ui = Ui_parentMenu()
    ui.setupUi(parentMenu)
    parentMenu.show()
    sys.exit(app.exec_())
