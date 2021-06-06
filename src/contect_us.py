from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Contect_Us(object):
    def setupUi(self, Contect_Us):
        Contect_Us.setObjectName("Contect_Us")
        Contect_Us.resize(532, 248)
        self.Email = QtWidgets.QLabel(Contect_Us)
        self.Email.setGeometry(QtCore.QRect(70, 130, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Email.setFont(font)
        self.Email.setObjectName("Email")
        self.Close_bttn = QtWidgets.QPushButton(Contect_Us)
        self.Close_bttn.setGeometry(QtCore.QRect(420, 190, 93, 28))
        self.Close_bttn.setObjectName("Close_bttn")
        self.label = QtWidgets.QLabel(Contect_Us)
        self.label.setGeometry(QtCore.QRect(20, 10, 481, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Contect_Us)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Close_bttn.clicked.connect(Contect_Us.close)

        self.retranslateUi(Contect_Us)
        QtCore.QMetaObject.connectSlotsByName(Contect_Us)

    def retranslateUi(self, Contect_Us):
        _translate = QtCore.QCoreApplication.translate
        Contect_Us.setWindowTitle(_translate("Contect_Us", "Dialog"))
        self.Email.setText(_translate("Contect_Us", " support@SCE_Project.co.il"))
        self.Close_bttn.setText(_translate("Contect_Us", "Close"))
        self.label.setText(_translate("Contect_Us", "if you have any question or suggestion"))
        self.label_2.setText(_translate("Contect_Us", " feel free to contect us in the Email below:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Parent_Registered = QtWidgets.QDialog()
    ui = Ui_Contect_Us()
    ui.setupUi(Parent_Registered)
    Parent_Registered.show()
    sys.exit(app.exec_())
