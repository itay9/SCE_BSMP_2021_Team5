from PyQt5 import QtCore, QtGui, QtWidgets
import MainMenu


class Ui_Login_Success(object):

    def setupUi(self, Login_Success):
        Login_Success.setObjectName("Login_Success")
        Login_Success.resize(301, 123)
        self.Success_Meesage = QtWidgets.QLabel(Login_Success)
        self.Success_Meesage.setGeometry(QtCore.QRect(20, -10, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Success_Meesage.setFont(font)
        self.Success_Meesage.setObjectName("Success_Meesage")
        self.Close_bttn = QtWidgets.QPushButton(Login_Success)
        self.Close_bttn.setGeometry(QtCore.QRect(100, 80, 93, 28))
        self.Close_bttn.setObjectName("Close_bttn")

        self.Close_bttn.clicked.connect(Login_Success.close)

        self.retranslateUi(Login_Success)
        QtCore.QMetaObject.connectSlotsByName(Login_Success)

    def retranslateUi(self, Login_Success):
        _translate = QtCore.QCoreApplication.translate
        Login_Success.setWindowTitle(_translate("Login_Success", "Dialog"))
        self.Success_Meesage.setText(_translate("Login_Success", "Login Successfully"))
        self.Close_bttn.setText(_translate("Login_Success", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Success = QtWidgets.QDialog()
    ui = Ui_Login_Success()
    ui.setupUi(Login_Success)
    Login_Success.show()
    sys.exit(app.exec_())
