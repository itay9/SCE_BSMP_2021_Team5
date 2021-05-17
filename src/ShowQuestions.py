from PyQt5 import QtCore, QtGui, QtWidgets
import DB

class Ui_QuestionTable(object):
    def setupUi(self, QuestionTable):
        QuestionTable.setObjectName("QuestionTable")
        QuestionTable.resize(762, 466)
        self.centralwidget = QtWidgets.QWidget(QuestionTable)
        self.centralwidget.setObjectName("centralwidget")
        self.questionTable = QtWidgets.QTableWidget(self.centralwidget)
        self.questionTable.setGeometry(QtCore.QRect(30, 70, 711, 221))
        self.questionTable.setCornerButtonEnabled(False)
        self.questionTable.setObjectName("questionTable")
        self.questionTable.setColumnCount(7)
        self.questionTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.questionTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.questionTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.questionTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.questionTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.questionTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.questionTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.questionTable.setHorizontalHeaderItem(6, item)
        self.question_TABLE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.question_TABLE_LABEL.setGeometry(QtCore.QRect(120, 10, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.question_TABLE_LABEL.setFont(font)
        self.question_TABLE_LABEL.setObjectName("question_TABLE_LABEL")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(410, 300, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(600, 390, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.input_qid = QtWidgets.QLineEdit(self.centralwidget)
        self.input_qid.setGeometry(QtCore.QRect(260, 310, 113, 22))
        self.input_qid.setObjectName("input_qid")
        self.question_label_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.question_label_LABEL.setGeometry(QtCore.QRect(40, 300, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.question_label_LABEL.setFont(font)
        self.question_label_LABEL.setObjectName("question_label_LABEL")
        self.add_new_question_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_question_button.setGeometry(QtCore.QRect(30, 380, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_new_question_button.setFont(font)
        self.add_new_question_button.setObjectName("add_new_question_button")
        QuestionTable.setCentralWidget(self.centralwidget)
        self.load_data() # load data
        #bttn
        self.backButton.clicked.connect(QuestionTable.close)
        self.deleteButton.clicked.connect(self.delete_question)

        self.retranslateUi(QuestionTable)
        QtCore.QMetaObject.connectSlotsByName(QuestionTable)

    def load_data(self):
        '''

        Returns: load data to table

        '''
        results = DB.get_all_questions()
        self.questionTable.setRowCount(len(results)) #updats table rows
        for i in range(len(results)):
            data = results[i]
            self.questionTable.setItem(i,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.questionTable.setItem(i,1,QtWidgets.QTableWidgetItem(data[1]))
            self.questionTable.setItem(i,2,QtWidgets.QTableWidgetItem(str(data[7])))
            self.questionTable.setItem(i,3,QtWidgets.QTableWidgetItem(data[3]))
            self.questionTable.setItem(i, 4, QtWidgets.QTableWidgetItem(data[4]))
            self.questionTable.setItem(i, 5, QtWidgets.QTableWidgetItem(data[5]))
            self.questionTable.setItem(i, 6, QtWidgets.QTableWidgetItem(data[6]))

    def delete_question(self):
        '''


        Returns: delete question from DB

        '''
        qid = self.input_qid.text()
        DB.remove_question(qid)
        self.load_data()


    def retranslateUi(self, QuestionTable):
        _translate = QtCore.QCoreApplication.translate
        QuestionTable.setWindowTitle(_translate("QuestionTable", "MainWindow"))
        item = self.questionTable.horizontalHeaderItem(0)
        item.setText(_translate("QuestionTable", "Qid"))
        item = self.questionTable.horizontalHeaderItem(1)
        item.setText(_translate("QuestionTable", "word"))
        item = self.questionTable.horizontalHeaderItem(2)
        item.setText(_translate("QuestionTable", "answer"))
        item = self.questionTable.horizontalHeaderItem(3)
        item.setText(_translate("QuestionTable", "choice 1"))
        item = self.questionTable.horizontalHeaderItem(4)
        item.setText(_translate("QuestionTable", "choice 2"))
        item = self.questionTable.horizontalHeaderItem(5)
        item.setText(_translate("QuestionTable", "choice 3"))
        item = self.questionTable.horizontalHeaderItem(6)
        item.setText(_translate("QuestionTable", "choice 4"))
        self.question_TABLE_LABEL.setText(_translate("QuestionTable", "<html><head/><body><p><span style=\" text-decoration: underline;\">Question Table</span></p></body></html>"))
        self.deleteButton.setText(_translate("QuestionTable", "Delete"))
        self.backButton.setText(_translate("QuestionTable", "Back"))
        self.question_label_LABEL.setText(_translate("QuestionTable", "Enter Question ID :"))
        self.add_new_question_button.setText(_translate("QuestionTable", "Add New Question"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QuestionTable = QtWidgets.QMainWindow()
    ui = Ui_QuestionTable()
    ui.setupUi(QuestionTable)
    QuestionTable.show()
    sys.exit(app.exec_())
