# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#2F4F4F")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 521, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#F0FFF0\n"
"")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 161, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("системы счисл.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(670, 130, 151, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("валюты.png"))
        self.label_4.setObjectName("label_4")
        self.input_kursval1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_kursval1.setGeometry(QtCore.QRect(610, 240, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.input_kursval1.setFont(font)
        self.input_kursval1.setStyleSheet("background-color:#2F4F4F;\n"
"border: 3px solid #778899;\n"
"color: white")
        self.input_kursval1.setText("")
        self.input_kursval1.setAlignment(QtCore.Qt.AlignCenter)
        self.input_kursval1.setObjectName("input_kursval1")
        self.pushButtonkursval = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonkursval.setGeometry(QtCore.QRect(610, 550, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonkursval.setFont(font)
        self.pushButtonkursval.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color: #2F4F4F;\n"
"    border-radius: 30;\n"
"    border: 3px solid #778899;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: #ff4545;\n"
"    color: black;\n"
"}")
        self.pushButtonkursval.setObjectName("pushButtonkursval")
        self.input_kursval2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_kursval2.setGeometry(QtCore.QRect(610, 320, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.input_kursval2.setFont(font)
        self.input_kursval2.setStyleSheet("background-color:#2F4F4F;\n"
"border: 3px solid #778899;\n"
"color: white")
        self.input_kursval2.setText("")
        self.input_kursval2.setAlignment(QtCore.Qt.AlignCenter)
        self.input_kursval2.setObjectName("input_kursval2")
        self.output_kursval1 = QtWidgets.QLineEdit(self.centralwidget)
        self.output_kursval1.setGeometry(QtCore.QRect(610, 400, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.output_kursval1.setFont(font)
        self.output_kursval1.setStyleSheet("background-color:#2F4F4F;\n"
"border: 3px solid #778899;\n"
"color: white")
        self.output_kursval1.setText("")
        self.output_kursval1.setAlignment(QtCore.Qt.AlignCenter)
        self.output_kursval1.setObjectName("output_kursval1")
        self.output_kursval2 = QtWidgets.QLineEdit(self.centralwidget)
        self.output_kursval2.setGeometry(QtCore.QRect(610, 480, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.output_kursval2.setFont(font)
        self.output_kursval2.setStyleSheet("background-color:#2F4F4F;\n"
"border: 3px solid #778899;\n"
"color: white")
        self.output_kursval2.setText("")
        self.output_kursval2.setAlignment(QtCore.Qt.AlignCenter)
        self.output_kursval2.setObjectName("output_kursval2")
        self.output_rasst2 = QtWidgets.QLineEdit(self.centralwidget)
        self.output_rasst2.setGeometry(QtCore.QRect(40, 480, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.output_rasst2.setFont(font)
        self.output_rasst2.setStyleSheet("background-color:#2F4F4F;\n"
"border: 3px solid #778899;\n"
"color: white")
        self.output_rasst2.setText("")
        self.output_rasst2.setAlignment(QtCore.Qt.AlignCenter)
        self.output_rasst2.setObjectName("output_rasst2")
        self.input_rasst2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_rasst2.setGeometry(QtCore.QRect(40, 320, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.input_rasst2.setFont(font)
        self.input_rasst2.setStyleSheet("background-color:#2F4F4F;\n"
"border: 3px solid #778899;\n"
"color: white")
        self.input_rasst2.setText("")
        self.input_rasst2.setAlignment(QtCore.Qt.AlignCenter)
        self.input_rasst2.setObjectName("input_rasst2")
        self.pushButtonrasst = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonrasst.setGeometry(QtCore.QRect(40, 560, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonrasst.setFont(font)
        self.pushButtonrasst.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color: #2F4F4F;\n"
"    border-radius: 30;\n"
"    border: 3px solid #778899;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: #ff4545;\n"
"    color: black;\n"
"}")
        self.pushButtonrasst.setObjectName("pushButtonrasst")
        self.input_rasst1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_rasst1.setGeometry(QtCore.QRect(40, 240, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.input_rasst1.setFont(font)
        self.input_rasst1.setStyleSheet("background-color:#2F4F4F;\n"
"border: 3px solid #778899;\n"
"color: white")
        self.input_rasst1.setText("")
        self.input_rasst1.setAlignment(QtCore.Qt.AlignCenter)
        self.input_rasst1.setObjectName("input_rasst1")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 400, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:#2F4F4F;\n"
"border: 3px solid #778899;\n"
"color: white")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 130, 251, 211))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("системкомп.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 380, 231, 221))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("графвалдоллар.jpg"))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 21))
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
        self.label.setText(_translate("MainWindow", "Перевод единиц измерения"))
        self.pushButtonkursval.setText(_translate("MainWindow", "ПЕРЕВОДИ"))
        self.pushButtonrasst.setText(_translate("MainWindow", "ПЕРЕВОДИ"))
        self.label_5.setText(_translate("MainWindow", "В 10 СИСТЕМУ СЧИСЛЕНИЯ"))
