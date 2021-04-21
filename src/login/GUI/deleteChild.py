from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import ParentMenu
import DB

class Ui_ChildTableDelete(object):

    def rtrn_ParentMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ParentMenu.Ui_parentMenu()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, ChildTableDelete):
        ChildTableDelete.setObjectName("ChildTableDelete")
        ChildTableDelete.resize(670, 459)
        self.centralwidget = QtWidgets.QWidget(ChildTableDelete)
        self.centralwidget.setObjectName("centralwidget")
        self.childTable = QtWidgets.QTableWidget(self.centralwidget)
        self.childTable.setGeometry(QtCore.QRect(180, 70, 271, 221))
        self.childTable.setCornerButtonEnabled(False)
        self.childTable.setObjectName("childTable")
        self.childTable.setColumnCount(2)
        self.childTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.childTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.childTable.setHorizontalHeaderItem(1, item)
        self.Child_TABLE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.Child_TABLE_LABEL.setGeometry(QtCore.QRect(150, 10, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Child_TABLE_LABEL.setFont(font)
        self.Child_TABLE_LABEL.setObjectName("Child_TABLE_LABEL")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(250, 360, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setObjectName("DeleteButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)

        self.BackButton.clicked.connect(self.rtrn_ParentMenu)
        self.BackButton.clicked.connect(ChildTableDelete.close)

        self.BackButton.setGeometry(QtCore.QRect(510, 380, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.inputChildName = QtWidgets.QLineEdit(self.centralwidget)
        self.inputChildName.setGeometry(QtCore.QRect(260, 310, 113, 22))
        self.inputChildName.setObjectName("inputChildName")
        self.child_NAME_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.child_NAME_LABEL.setGeometry(QtCore.QRect(40, 300, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.child_NAME_LABEL.setFont(font)
        self.child_NAME_LABEL.setObjectName("child_NAME_LABEL")
        ChildTableDelete.setCentralWidget(self.centralwidget)

        #get data
        self.load_data()
        self.DeleteButton.clicked.connect(self.delete_child)
        self.retranslateUi(ChildTableDelete)
        QtCore.QMetaObject.connectSlotsByName(ChildTableDelete)

    def load_data(self):
        result = DB.get_data_kid_by_parent(DB.currentUser)
        self.childTable.setRowCount(len(result))
        for row_num in  range(len(result)):
            row = result[row_num]
            self.childTable.setItem(row_num,0,QtWidgets.QTableWidgetItem(row[0]))
            self.childTable.setItem(row_num, 1, QtWidgets.QTableWidgetItem(row[1]))

    def delete_child(self):
        name_to_delete = self.inputChildName.text()
        DB.remove_user(name_to_delete)
        self.load_data()

    def retranslateUi(self, ChildTableDelete):
        _translate = QtCore.QCoreApplication.translate
        ChildTableDelete.setWindowTitle(_translate("ChildTableDelete", "MainWindow"))
        item = self.childTable.horizontalHeaderItem(0)
        item.setText(_translate("ChildTableDelete", "Username"))
        item = self.childTable.horizontalHeaderItem(1)
        item.setText(_translate("ChildTableDelete", "Password"))
        self.Child_TABLE_LABEL.setText(_translate("ChildTableDelete",
                                                  "<html><head/><body><p><span style=\" text-decoration: underline;\">My Children Table</span></p></body></html>"))
        self.DeleteButton.setText(_translate("ChildTableDelete", "Delete"))
        self.BackButton.setText(_translate("ChildTableDelete", "Back"))
        self.child_NAME_LABEL.setText(_translate("ChildTableDelete", "Enter Childs Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChildTableDelete = QtWidgets.QMainWindow()
    ui = Ui_ChildTableDelete()
    ui.setupUi(ChildTableDelete)
    ChildTableDelete.show()
    sys.exit(app.exec_())
