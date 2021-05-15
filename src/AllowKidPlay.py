from PyQt5 import QtCore, QtGui, QtWidgets
import DB

class Ui_AllowKidPlay(object):
    def setupUi(self, AllowKidPlay):
        AllowKidPlay.setObjectName("AllowKidPlay")
        AllowKidPlay.resize(670, 459)
        self.centralwidget = QtWidgets.QWidget(AllowKidPlay)
        self.centralwidget.setObjectName("centralwidget")
        self.childTable = QtWidgets.QTableWidget(self.centralwidget)
        self.childTable.setGeometry(QtCore.QRect(100, 70, 351, 221))
        self.childTable.setCornerButtonEnabled(False)
        self.childTable.setObjectName("childTable")
        self.childTable.setColumnCount(3)
        self.childTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.childTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.childTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.childTable.setHorizontalHeaderItem(2, item)
        self.parent_TABLE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.parent_TABLE_LABEL.setGeometry(QtCore.QRect(120, 10, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.parent_TABLE_LABEL.setFont(font)
        self.parent_TABLE_LABEL.setObjectName("parent_TABLE_LABEL")
        self.allowButton = QtWidgets.QPushButton(self.centralwidget)
        self.allowButton.setGeometry(QtCore.QRect(250, 360, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.allowButton.setFont(font)
        self.allowButton.setObjectName("allowButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(510, 380, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.input_kid_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_kid_name.setGeometry(QtCore.QRect(260, 310, 113, 22))
        self.input_kid_name.setObjectName("input_kid_name")
        self.kid_NAME_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.kid_NAME_LABEL.setGeometry(QtCore.QRect(40, 300, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kid_NAME_LABEL.setFont(font)
        self.kid_NAME_LABEL.setObjectName("kid_NAME_LABEL")
        AllowKidPlay.setCentralWidget(self.centralwidget)
        #bttn
        self.load_data()
        self.allowButton.clicked.connect(self.allow_user)
        self.backButton.clicked.connect(AllowKidPlay.close)

        self.retranslateUi(AllowKidPlay)
        QtCore.QMetaObject.connectSlotsByName(AllowKidPlay)

    def load_data(self):
        result = DB.get_data_kid()
        self.childTable.setRowCount(len(result))
        for row_num in range(len(result)):
            row = result[row_num]
            if row[5] == 1:
                allow = "True"
            else:
                allow= "False"
            self.childTable.setItem(row_num,0,QtWidgets.QTableWidgetItem(row[0]))
            self.childTable.setItem(row_num, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.childTable.setItem(row_num, 2, QtWidgets.QTableWidgetItem(allow))

    def allow_user(self):
        user = self.input_kid_name.text()
        DB.allowPlay(user)
        self.load_data()

    def retranslateUi(self, AllowKidPlay):
        _translate = QtCore.QCoreApplication.translate
        AllowKidPlay.setWindowTitle(_translate("AllowKidPlay", "MainWindow"))
        item = self.childTable.horizontalHeaderItem(0)
        item.setText(_translate("AllowKidPlay", "Username"))
        item = self.childTable.horizontalHeaderItem(1)
        item.setText(_translate("AllowKidPlay", "Password"))
        item = self.childTable.horizontalHeaderItem(2)
        item.setText(_translate("AllowKidPlay", "Can Play"))
        self.parent_TABLE_LABEL.setText(_translate("AllowKidPlay", "<html><head/><body><p><span style=\" text-decoration: underline;\">child table</span></p></body></html>"))
        self.allowButton.setText(_translate("AllowKidPlay", "Allow"))
        self.backButton.setText(_translate("AllowKidPlay", "Back"))
        self.kid_NAME_LABEL.setText(_translate("AllowKidPlay", "Enter child  Name:"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AllowKidPlay = QtWidgets.QMainWindow()
    ui = Ui_AllowKidPlay()
    ui.setupUi(AllowKidPlay)
    AllowKidPlay.show()
    sys.exit(app.exec_())
