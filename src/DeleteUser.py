from PyQt5 import QtCore, QtGui, QtWidgets
import DB


class Ui_DeleteUser(object):
    def setupUi(self, DeleteUser):
        DeleteUser.setObjectName("DeleteUser")
        DeleteUser.resize(670, 459)
        self.centralwidget = QtWidgets.QWidget(DeleteUser)
        self.centralwidget.setObjectName("centralwidget")
        self.userTable = QtWidgets.QTableWidget(self.centralwidget)
        self.userTable.setGeometry(QtCore.QRect(100, 70, 420, 221))
        self.userTable.setCornerButtonEnabled(False)
        self.userTable.setObjectName("userTable")
        self.userTable.setColumnCount(4)
        self.userTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(3, item)
        self.user_TABLE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.user_TABLE_LABEL.setGeometry(QtCore.QRect(120, 10, 241, 61))

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.user_TABLE_LABEL.setFont(font)
        self.user_TABLE_LABEL.setObjectName("user_TABLE_LABEL")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(250, 360, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(510, 380, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.input_user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_user_name.setGeometry(QtCore.QRect(260, 310, 113, 22))
        self.input_user_name.setObjectName("input_user_name")
        self.user_NAME_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.user_NAME_LABEL.setGeometry(QtCore.QRect(40, 300, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.user_NAME_LABEL.setFont(font)
        self.user_NAME_LABEL.setObjectName("user_NAME_LABEL")
        DeleteUser.setCentralWidget(self.centralwidget)
        #bttn
        self.backButton.clicked.connect(DeleteUser.close)
        self.load_data()
        self.deleteButton.clicked.connect(self.delete_user)


        self.retranslateUi(DeleteUser)
        QtCore.QMetaObject.connectSlotsByName(DeleteUser)

    def load_data(self):
        result = DB.get_data_all_users()
        self.userTable.setRowCount(len(result))
        for row_num in range(len(result)):
            row = result[row_num]
            self.userTable.setItem(row_num,0,QtWidgets.QTableWidgetItem(row[0]))
            self.userTable.setItem(row_num, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.userTable.setItem(row_num, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.userTable.setItem(row_num, 3, QtWidgets.QTableWidgetItem(row[3]))
    def delete_user(self):
        user = self.input_user_name.text()
        DB.remove_user(user)
        self.load_data()

    def retranslateUi(self, DeleteUser):
        _translate = QtCore.QCoreApplication.translate
        DeleteUser.setWindowTitle(_translate("DeleteUser", "MainWindow"))
        item = self.userTable.horizontalHeaderItem(0)
        item.setText(_translate("DeleteUser", "Username"))
        item = self.userTable.horizontalHeaderItem(1)
        item.setText(_translate("DeleteUser", "Password"))
        item = self.userTable.horizontalHeaderItem(2)
        item.setText(_translate("DeleteUser", "Type"))
        item = self.userTable.horizontalHeaderItem(3)
        item.setText(_translate("DeleteUser", "Parent Name"))
        self.user_TABLE_LABEL.setText(_translate("DeleteUser", "<html><head/><body><p><span style=\" text-decoration: underline;\">Users table</span></p></body></html>"))
        self.deleteButton.setText(_translate("DeleteUser", "Delete"))
        self.backButton.setText(_translate("DeleteUser", "Back"))
        self.user_NAME_LABEL.setText(_translate("DeleteUser", "Enter user  Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteUser = QtWidgets.QMainWindow()
    ui = Ui_DeleteUser()
    ui.setupUi(DeleteUser)
    DeleteUser.show()
    sys.exit(app.exec_())
