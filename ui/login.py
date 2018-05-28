# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(713, 412)
        Dialog.setAutoFillBackground(True)
        palette = QtGui.QPalette()
        palette.setBrush(Dialog.backgroundRole(),QtGui.QBrush(QtGui.QImage("./resource/imgback/back.jpg").scaled(Dialog.size())))
        Dialog.setPalette(palette)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 120, 60, 30))
        self.label.setStyleSheet("border-image: \\*url();\n"
"font: 12pt \"Sans Serif\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 210, 60, 30))
        self.label_2.setStyleSheet("border-image: \\*url();\n"
"font: 12pt \"Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.textEdit_username = QtWidgets.QLineEdit(Dialog)
        self.textEdit_username.setGeometry(QtCore.QRect(280, 120, 245, 35))
        self.textEdit_username.setStyleSheet("border-image: \\*url();\n"
"font: 12pt \"Sans Serif\";")
        self.textEdit_username.setObjectName("textEdit_username")
        self.textEdit_userpasswd = QtWidgets.QLineEdit(Dialog)
        self.textEdit_userpasswd.setGeometry(QtCore.QRect(280, 210, 245, 35))
        self.textEdit_userpasswd.setStyleSheet("border-image: \\*url();\n"
"font: 12pt \"Sans Serif\";")
        self.textEdit_userpasswd.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textEdit_userpasswd.setPlaceholderText("密码6-15位，只能有数字和字母")
        self.textEdit_userpasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textEdit_userpasswd.setObjectName("textEdit_userpasswd")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 310, 90, 30))
        self.pushButton.setStyleSheet("border-image: \\*url();\n"
"font: 12pt \"Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 310, 90, 30))
        self.pushButton_2.setStyleSheet("border-image: \\*url();\n"
"font: 12pt \"Sans Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Ui_Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "用户名："))
        self.label_2.setText(_translate("Dialog", " 密码  ："))
        self.pushButton.setText(_translate("Dialog", "登录"))
        self.pushButton_2.setText(_translate("Dialog", "清空"))
 

