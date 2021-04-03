from PyQt5 import QtCore, QtGui, QtWidgets
import ParentRegister


class Ui_Parent_Registered(object):

    # def rtrn_mainMenu(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = MainMenu.Ui_mainMenu()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    def setupUi(self, Parent_Registered):
        Parent_Registered.setObjectName("Parent_Registered")
        Parent_Registered.resize(301, 123)
        self.Success_Meesage = QtWidgets.QLabel(Parent_Registered)
        self.Success_Meesage.setGeometry(QtCore.QRect(20, -10, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Success_Meesage.setFont(font)
        self.Success_Meesage.setObjectName("Success_Meesage")
        self.Close_bttn = QtWidgets.QPushButton(Parent_Registered)
        self.Close_bttn.setGeometry(QtCore.QRect(100, 80, 93, 28))
        self.Close_bttn.setObjectName("Close_bttn")

        #self.Close_bttn.clicked.connect(self.rtrn_mainMenu)

        self.retranslateUi(Parent_Registered)
        QtCore.QMetaObject.connectSlotsByName(Parent_Registered)

    def retranslateUi(self, Parent_Registered):
        _translate = QtCore.QCoreApplication.translate
        Parent_Registered.setWindowTitle(_translate("Parent_Registered", "Dialog"))
        self.Success_Meesage.setText(_translate("Parent_Registered", "Registered Successfully"))
        self.Close_bttn.setText(_translate("Parent_Registered", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Parent_Registered = QtWidgets.QDialog()
    ui = Ui_Parent_Registered()
    ui.setupUi(Parent_Registered)
    Parent_Registered.show()
    sys.exit(app.exec_())
