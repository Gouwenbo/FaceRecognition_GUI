# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager_user.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManagerUser_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_ManagerUser_Dialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, ManagerUser_Dialog):
        ManagerUser_Dialog.setObjectName("ManagerUser_Dialog")
        ManagerUser_Dialog.resize(800, 460)
        font = QtGui.QFont()
        font.setPointSize(10)
        ManagerUser_Dialog.setFont(font)
        palette = QtGui.QPalette()
        palette.setBrush(ManagerUser_Dialog.backgroundRole(),QtGui.QBrush(QtGui.QImage("./resource/imgback/back.jpg").scaled(ManagerUser_Dialog.size())))
        ManagerUser_Dialog.setPalette(palette)
        self.label = QtWidgets.QLabel(ManagerUser_Dialog)
        self.label.setGeometry(QtCore.QRect(440, 80, 59, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ManagerUser_Dialog)
        self.label_2.setGeometry(QtCore.QRect(440, 140, 59, 14))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ManagerUser_Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 200, 59, 14))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ManagerUser_Dialog)
        self.label_4.setGeometry(QtCore.QRect(440, 260, 59, 14))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QLineEdit(ManagerUser_Dialog)
        self.textEdit.setGeometry(QtCore.QRect(520, 75, 211, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QLineEdit(ManagerUser_Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(520, 133, 211, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QLineEdit(ManagerUser_Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(520, 190, 211, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(ManagerUser_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(455, 340, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ManagerUser_Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 340, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(ManagerUser_Dialog)
        self.radioButton.setGeometry(QtCore.QRect(520, 260, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(ManagerUser_Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(630, 260, 101, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_5 = QtWidgets.QLabel(ManagerUser_Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 80, 20))
        self.label_5.setObjectName("label_5")

        self.tableView = QtWidgets.QTableView(ManagerUser_Dialog)
        self.tableView.setGeometry(QtCore.QRect(5, 61, 421, 321))
        self.tableView.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        self.retranslateUi(ManagerUser_Dialog)
        QtCore.QMetaObject.connectSlotsByName(ManagerUser_Dialog)

    def retranslateUi(self, ManagerUser_Dialog):
        _translate = QtCore.QCoreApplication.translate
        ManagerUser_Dialog.setWindowTitle(_translate("ManagerUser_Dialog", "用户管理"))
        self.label.setText(_translate("ManagerUser_Dialog", "用户ID"))
        self.label_2.setText(_translate("ManagerUser_Dialog", "用户姓名"))
        self.label_3.setText(_translate("ManagerUser_Dialog", "用户密码"))
        self.label_4.setText(_translate("ManagerUser_Dialog", "用户权限"))
        self.pushButton.setText(_translate("ManagerUser_Dialog", "添加用户"))
        self.pushButton_2.setText(_translate("ManagerUser_Dialog", "删除用户"))
        self.radioButton.setText(_translate("ManagerUser_Dialog", "Teacher"))
        self.radioButton_2.setText(_translate("ManagerUser_Dialog", "Student"))
        self.label_5.setText(_translate("ManagerUser_Dialog", "用户数据库："))

