# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class manager_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(manager_Dialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 460)
        palette = QtGui.QPalette()
        palette.setBrush(Dialog.backgroundRole(),QtGui.QBrush(QtGui.QImage("./resource/imgback/back.jpg").scaled(Dialog.size())))
        Dialog.setPalette(palette)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 130, 90, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 130, 90, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 130, 90, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 280, 90, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 280, 95, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(570, 280, 90, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(590, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(650, 33, 135, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "管理界面"))
        self.pushButton.setText(_translate("Dialog", "载入模型"))
        self.pushButton_2.setText(_translate("Dialog", "载入ID"))
        self.pushButton_3.setText(_translate("Dialog", "开始考勤"))
        self.pushButton_4.setText(_translate("Dialog", "人员管理"))
        self.pushButton_5.setText(_translate("Dialog", "考勤查询"))
        self.pushButton_6.setText(_translate("Dialog", "增量ID"))
        self.label.setText(_translate("Dialog", "总人数："))

