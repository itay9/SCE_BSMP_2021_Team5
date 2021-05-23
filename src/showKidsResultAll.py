
from PyQt5 import QtCore, QtGui, QtWidgets
import DB


class Ui_KidsResultTable(object):
    def setupUi(self, KidsResultTable):
        KidsResultTable.setObjectName("KidsResultTable")
        KidsResultTable.resize(762, 466)
        self.centralwidget = QtWidgets.QWidget(KidsResultTable)
        self.centralwidget.setObjectName("centralwidget")
        self.resultTable = QtWidgets.QTableWidget(self.centralwidget)
        self.resultTable.setGeometry(QtCore.QRect(30, 70, 551, 361))
        self.resultTable.setCornerButtonEnabled(False)
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(4)
        self.resultTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(3, item)
        self.result_TABLE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.result_TABLE_LABEL.setGeometry(QtCore.QRect(120, 10, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.result_TABLE_LABEL.setFont(font)
        self.result_TABLE_LABEL.setObjectName("result_TABLE_LABEL")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(600, 390, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setGeometry(QtCore.QRect(600, 310, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exportButton.setFont(font)
        self.exportButton.setObjectName("exportButton")
        KidsResultTable.setCentralWidget(self.centralwidget)

        self.load_data()
        self.backButton.clicked.connect(KidsResultTable.close)
        self.exportButton.clicked.connect(self.export_bttn)
        self.retranslateUi(KidsResultTable)
        QtCore.QMetaObject.connectSlotsByName(KidsResultTable)

    def export_bttn(self):
        DB.export_table_to_csv("results")

    def load_data(self):
        kids_data = DB.get_all_result()
        self.resultTable.setRowCount(len(kids_data))  # updats table rows
        for i in range(len(kids_data)):
                data = kids_data[i]
                self.resultTable.setItem(i,0,QtWidgets.QTableWidgetItem(str(data[0])))
                self.resultTable.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data[1])))
                self.resultTable.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data[2])))
                self.resultTable.setItem(i, 3, QtWidgets.QTableWidgetItem(str(int(data[3]*100))+"%"))

    def retranslateUi(self, KidsResultTable):
        _translate = QtCore.QCoreApplication.translate
        KidsResultTable.setWindowTitle(_translate("KidsResultTable", "MainWindow"))
        item = self.resultTable.horizontalHeaderItem(0)
        item.setText(_translate("KidsResultTable", "Kid name"))
        item = self.resultTable.horizontalHeaderItem(1)
        item.setText(_translate("KidsResultTable", "Date"))
        item = self.resultTable.horizontalHeaderItem(2)
        item.setText(_translate("KidsResultTable", "Game #"))
        item = self.resultTable.horizontalHeaderItem(3)
        item.setText(_translate("KidsResultTable", "Success rate"))
        self.result_TABLE_LABEL.setText(_translate("KidsResultTable", "<html><head/><body><p><span style=\" text-decoration: underline;\">Kids Result Table</span></p></body></html>"))
        self.backButton.setText(_translate("KidsResultTable", "Back"))
        self.exportButton.setText(_translate("KidsResultTable", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KidsResultTable = QtWidgets.QMainWindow()
    ui = Ui_KidsResultTable()
    ui.setupUi(KidsResultTable)
    KidsResultTable.show()
    sys.exit(app.exec_())