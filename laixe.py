# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laixe.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 426)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 350, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 350, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 340, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 10, 160, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 381, 321))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Lùi"))
        self.pushButton_2.setText(_translate("MainWindow", "Tiến"))
        self.pushButton_3.setText(_translate("MainWindow", "Nộp bài"))
        self.radioButton_2.setText(_translate("MainWindow", "A"))
        self.radioButton_3.setText(_translate("MainWindow", "B"))
        self.radioButton_4.setText(_translate("MainWindow", "C"))
        self.radioButton.setText(_translate("MainWindow", "D"))

    def control(self, MainWindow):
        string = self.text()
        self.textBrowser.setText(string[self.i])

        self.pushButton_2.clicked.connect(self.next)

        self.pushButton.clicked.connect(self.prev)

        self.radioButton_2.clicked.connect(self.c_a)
        self.radioButton_3.clicked.connect(self.c_b)
        self.radioButton_4.clicked.connect(self.c_c)
        self.radioButton.clicked.connect(self.c_d)

        self.pushButton_3.clicked.connect(self.announce)

    def calculate(self):
        with open('Ans.txt', encoding='utf-8-sig', mode='r') as f:
            cor = f.readlines()
        cor = [x.strip() for x in cor]

        final = self.ans()
        total_num_wr = 0
        ques_wrong = []
        for x in range(len(self.text())):
            if final[x] != cor[x][-1:]:
                total_num_wr += 1
                ques_wrong.append(x + 1)

        # CALCULATE TOTAL SCORE AND EVALUATE
        total_num_cor = len(self.text()) - total_num_wr
        return total_num_cor

    def announce(self):
        mbox = QMessageBox()

        cor = self.calculate()
        if cor >= 2:
            mbox.setText("Your allegiance has been noted")
            mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            mbox.exec_()

    def text(self):
        ques = []
        with open('Ques.txt', encoding='utf-8-sig', mode='r') as f:
            ques = f.readlines()
        ques = [x.strip() for x in ques]
        ques.append('')
        # READ DATA FROM FILE

        check = ['A', 'B', 'C', 'D']
        total = 1
        string = []
        tmp = ''
        for i in range(len(ques)):
            tmp += ques[i] + '\n'
            if ques[i] == '':
                string.append(tmp)
                tmp = ''
        print(string)
        return string

    i = 0

    def next(self):
        self.i += 1

        return self.display(self.i)

    def prev(self):
        self.i -= 1
        return self.display(self.i)

    def display(self, i):
        string = self.text()
        self.textBrowser.setText(string[i])

    def ans(self):
        answer = [] * (len(self.text()) - 1)
        return answer

    def c_a(self):
        a_list = self.ans()
        a_list.append('a')
        return a_list

    def c_b(self):
        a_list = self.ans()
        a_list.append('b')
        return a_list

    def c_c(self):
        a_list = self.ans()
        a_list.append('c')
        return a_list

    def c_d(self):
        a_list = self.ans()
        a_list.append('d')
        return a_list

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.control(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
