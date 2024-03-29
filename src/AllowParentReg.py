from PyQt5 import QtCore, QtGui, QtWidgets
import DB

class Ui_AllowParentReg(object):
    def setupUi(self, AllowParentReg):
        AllowParentReg.setObjectName("AllowParentReg")
        AllowParentReg.resize(670, 459)
        self.centralwidget = QtWidgets.QWidget(AllowParentReg)
        self.centralwidget.setObjectName("centralwidget")
        self.parentTable = QtWidgets.QTableWidget(self.centralwidget)
        self.parentTable.setGeometry(QtCore.QRect(100, 70, 351, 221))
        self.parentTable.setCornerButtonEnabled(False)
        self.parentTable.setObjectName("parentTable")
        self.parentTable.setColumnCount(3)
        self.parentTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.parentTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.parentTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.parentTable.setHorizontalHeaderItem(2, item)
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
        self.input_parent_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_parent_name.setGeometry(QtCore.QRect(260, 310, 113, 22))
        self.input_parent_name.setObjectName("input_parent_name")
        self.parent_NAME_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.parent_NAME_LABEL.setGeometry(QtCore.QRect(40, 300, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parent_NAME_LABEL.setFont(font)
        self.parent_NAME_LABEL.setObjectName("parent_NAME_LABEL")
        AllowParentReg.setCentralWidget(self.centralwidget)
        #load data
        self.load_data()

        #bttn
        self.allowButton.clicked.connect(self.allow_user)
        self.retranslateUi(AllowParentReg)
        self.backButton.clicked.connect(AllowParentReg.close)
        QtCore.QMetaObject.connectSlotsByName(AllowParentReg)

    def load_data(self):
        result = DB.get_data_parent()
        self.parentTable.setRowCount(len(result))
        for row_num in range(len(result)):
            row = result[row_num]
            if row[4] == 1:
                allow = "True"
            else:
                allow= "False"
            self.parentTable.setItem(row_num,0,QtWidgets.QTableWidgetItem(row[0]))
            self.parentTable.setItem(row_num, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.parentTable.setItem(row_num, 2, QtWidgets.QTableWidgetItem(allow))
    def allow_user(self):
        user = self.input_parent_name.text()
        DB.allowReg(user)
        self.load_data()


    def retranslateUi(self, AllowParentReg):
        _translate = QtCore.QCoreApplication.translate
        AllowParentReg.setWindowTitle(_translate("AllowParentReg", "MainWindow"))
        item = self.parentTable.horizontalHeaderItem(0)
        item.setText(_translate("AllowParentReg", "Username"))
        item = self.parentTable.horizontalHeaderItem(1)
        item.setText(_translate("AllowParentReg", "Password"))
        item = self.parentTable.horizontalHeaderItem(2)
        item.setText(_translate("AllowParentReg", "Can Reg"))
        self.parent_TABLE_LABEL.setText(_translate("AllowParentReg", "<html><head/><body><p><span style=\" text-decoration: underline;\">Parent table</span></p></body></html>"))
        self.allowButton.setText(_translate("AllowParentReg", "Allow"))
        self.backButton.setText(_translate("AllowParentReg", "Back"))
        self.parent_NAME_LABEL.setText(_translate("AllowParentReg", "Enter Parent Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AllowParentReg = QtWidgets.QMainWindow()
    ui = Ui_AllowParentReg()
    ui.setupUi(AllowParentReg)
    AllowParentReg.show()
    sys.exit(app.exec_())
