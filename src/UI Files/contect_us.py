# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contect_us.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Parent_Registered(object):
    def setupUi(self, Parent_Registered):
        Parent_Registered.setObjectName("Parent_Registered")
        Parent_Registered.resize(532, 248)
        self.Email = QtWidgets.QLabel(Parent_Registered)
        self.Email.setGeometry(QtCore.QRect(70, 130, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Email.setFont(font)
        self.Email.setObjectName("Email")
        self.Close_bttn = QtWidgets.QPushButton(Parent_Registered)
        self.Close_bttn.setGeometry(QtCore.QRect(420, 190, 93, 28))
        self.Close_bttn.setObjectName("Close_bttn")
        self.label = QtWidgets.QLabel(Parent_Registered)
        self.label.setGeometry(QtCore.QRect(20, 10, 481, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Parent_Registered)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Parent_Registered)
        QtCore.QMetaObject.connectSlotsByName(Parent_Registered)

    def retranslateUi(self, Parent_Registered):
        _translate = QtCore.QCoreApplication.translate
        Parent_Registered.setWindowTitle(_translate("Parent_Registered", "Dialog"))
        self.Email.setText(_translate("Parent_Registered", " support@SCE_Project.co.il"))
        self.Close_bttn.setText(_translate("Parent_Registered", "Close"))
        self.label.setText(_translate("Parent_Registered", "if you have any question or suggestion"))
        self.label_2.setText(_translate("Parent_Registered", " feel free to contect us in the Email below:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Parent_Registered = QtWidgets.QDialog()
    ui = Ui_Parent_Registered()
    ui.setupUi(Parent_Registered)
    Parent_Registered.show()
    sys.exit(app.exec_())
