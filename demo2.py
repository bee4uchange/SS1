# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laixe.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.i = 0
        self.string = []
        self.length = len(self.string)
        self.ans = list(range(3))
        self.total_num_wr = 0
        self.total_num_cor = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(10, 310, 75, 23))
        self.prevButton.setObjectName("prevButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(100, 310, 75, 23))
        self.nextButton.setObjectName("nextButton")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(280, 310, 111, 41))
        self.submitButton.setObjectName("submitButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 381, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.startButton.setObjectName("startButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 240, 348, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.aButton.setObjectName("aButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.aButton)
        self.horizontalLayout.addWidget(self.aButton)
        self.bButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.bButton.setObjectName("bButton")
        self.buttonGroup.addButton(self.bButton)
        self.horizontalLayout.addWidget(self.bButton)
        self.cButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.cButton.setObjectName("cButton")
        self.buttonGroup.addButton(self.cButton)
        self.horizontalLayout.addWidget(self.cButton)
        self.dButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.dButton.setObjectName("dButton")
        self.buttonGroup.addButton(self.dButton)
        self.horizontalLayout.addWidget(self.dButton)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 10, 51, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 21))
        self.label.setObjectName("label")
        self.restartButton = QtWidgets.QPushButton(self.centralwidget)
        self.restartButton.setGeometry(QtCore.QRect(310, 10, 75, 23))
        self.restartButton.setObjectName("restartButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startButton.clicked.connect(self.displayQues)

        self.nextButton.clicked.connect(self.next)

        self.prevButton.clicked.connect(self.prev)

        self.aButton.clicked.connect(self.addA)

        self.bButton.clicked.connect(self.addB)

        self.cButton.clicked.connect(self.addC)

        self.dButton.clicked.connect(self.addD)

        self.submitButton.clicked.connect(self.calcTotal)

    def displayQues(self):
        ques = []
        with open('Ques.txt', encoding='utf-8-sig', mode='r') as f:
            ques = f.readlines()
        ques = [x.strip() for x in ques]
        ques.append('')
        # READ DATA FROM FILE
        check = ['A', 'B', 'C', 'D']
        total = 1
        tmp = ''
        c = 0
        for i in range(len(ques)):
            tmp += ques[i] + '\n'

            if ques[i] == '':
                self.string.append(tmp)
                tmp = ''
                c += 1
        self.length = c
        self.i = 0
        self.reset()
        self.textBrowser.setText(self.string[self.i])
        print(self.string)
        print(c)

    def next(self):
        self.reset()
        if self.i == (self.length - 1):
            self.i = (self.length - 1)
        else:
            self.i += 1
            self.textBrowser.setText(self.string[self.i])

    def prev(self):
        self.reset()
        if self.i == 0:
            self.i = 0
        else:
            self.i -= 1
            self.textBrowser.setText(self.string[self.i])

    def addA(self):
        print(self.ans)
        self.ans[self.i] = 'A'
        print(self.ans)

    def addB(self):
        print(self.ans)
        self.ans[self.i] = 'B'
        print(self.ans)

    def addC(self):
        print(self.ans)
        self.ans[self.i] = 'C'
        print(self.ans)

    def addD(self):
        print(self.ans)
        self.ans[self.i] = 'D'
        print(self.ans)

    def reset(self):
        self.buttonGroup.setExclusive(False)
        self.aButton.setChecked(False)
        self.bButton.setChecked(False)
        self.cButton.setChecked(False)
        self.dButton.setChecked(False)
        self.buttonGroup.setExclusive(True)

    def calcTotal(self):
        with open('Ans.txt', encoding='utf-8-sig', mode='r') as f:
            cor = f.readlines()
        cor = [x.strip() for x in cor]

        ques_wrong = []
        for x in range(self.length):
            if self.ans[x] != cor[x][-1:]:
                self.total_num_wr += 1
                ques_wrong.append(x + 1)

        # CALCULATE TOTAL SCORE AND EVALUATE
        self.total_num_cor = self.length - self.total_num_wr

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("BẠN {} {}!".format("ĐÃ" if self.total_num_cor >= 2 else "KHÔNG", "VƯỢT QUA BÀI THI!"))
        msg.setInformativeText("Số câu đúng: {} \n"
                               "Số câu sai: {}".format(self.total_num_cor, self.total_num_wr))

        msg.setWindowTitle("Kết quả")
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Luyện thi bằng lái xe"))
        self.prevButton.setText(_translate("MainWindow", "Lùi"))
        self.nextButton.setText(_translate("MainWindow", "Tiến"))
        self.submitButton.setText(_translate("MainWindow", "Nộp bài"))
        self.startButton.setText(_translate("MainWindow", "Bắt đầu"))
        self.aButton.setText(_translate("MainWindow", "A"))
        self.bButton.setText(_translate("MainWindow", "B"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.dButton.setText(_translate("MainWindow", "D"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.label.setText(_translate("MainWindow", "Chọn đề"))
        self.restartButton.setText(_translate("MainWindow", "Thi lại"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
