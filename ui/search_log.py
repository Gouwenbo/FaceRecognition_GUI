# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_log.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Searchlog_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Searchlog_Dialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, Searchlog_Dialog):
        Searchlog_Dialog.setObjectName("Searchlog_Dialog")
        Searchlog_Dialog.resize(1092, 734)
        font = QtGui.QFont()
        font.setPointSize(10)
        Searchlog_Dialog.setFont(font)
        palette = QtGui.QPalette()
        palette.setBrush(Searchlog_Dialog.backgroundRole(),QtGui.QBrush(QtGui.QImage("./resource/imgback/back.jpg").scaled(Searchlog_Dialog.size())))
        Searchlog_Dialog.setPalette(palette)
        self.label = QtWidgets.QLabel(Searchlog_Dialog)
        self.label.setGeometry(QtCore.QRect(710, 70, 59, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_2.setGeometry(QtCore.QRect(710, 130, 59, 14))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Searchlog_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(870, 370, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 61, 20))
        self.label_5.setObjectName("label_5")
        self.tableView = QtWidgets.QTableView(Searchlog_Dialog)
        self.tableView.setGeometry(QtCore.QRect(5, 61, 611, 271))
        self.tableView.setObjectName("listView")
        self.lineEdit = QtWidgets.QLineEdit(Searchlog_Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(780, 60, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Searchlog_Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(780, 120, 251, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_3.setGeometry(QtCore.QRect(710, 180, 59, 14))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(Searchlog_Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(780, 170, 111, 30))
        self.dateEdit.setDate(QtCore.QDate(2018, 5, 7))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Searchlog_Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(930, 170, 101, 31))
        self.dateEdit_2.setDate(QtCore.QDate(2018, 5, 12))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_4 = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_4.setGeometry(QtCore.QRect(906, 172, 21, 21))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_6.setGeometry(QtCore.QRect(710, 230, 59, 14))
        self.label_6.setObjectName("label_6")
        self.pushButton_preweek = QtWidgets.QPushButton(Searchlog_Dialog)
        self.pushButton_preweek.setGeometry(QtCore.QRect(780, 220, 111, 31))
        self.pushButton_preweek.setObjectName("pushButton_preweek")
        self.pushButton_premonth = QtWidgets.QPushButton(Searchlog_Dialog)
        self.pushButton_premonth.setGeometry(QtCore.QRect(930, 220, 101, 31))
        self.pushButton_premonth.setObjectName("pushButton_premonth")
        self.timeEdit = QtWidgets.QTimeEdit(Searchlog_Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(780, 270, 111, 31))
        self.timeEdit.setMaximumTime(QtCore.QTime(11, 0, 0))
        self.timeEdit.setMinimumTime(QtCore.QTime(6, 0, 0))
        self.timeEdit.setCurrentSectionIndex(0)
        self.timeEdit.setTime(QtCore.QTime(7, 30, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.label_7 = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_7.setGeometry(QtCore.QRect(710, 300, 59, 14))
        self.label_7.setObjectName("label_7")
        self.timeEdit_2 = QtWidgets.QTimeEdit(Searchlog_Dialog)
        self.timeEdit_2.setGeometry(QtCore.QRect(930, 270, 111, 31))
        self.timeEdit_2.setMaximumTime(QtCore.QTime(11, 0, 0))
        self.timeEdit_2.setMinimumTime(QtCore.QTime(6, 0, 0))
        self.timeEdit_2.setTime(QtCore.QTime(9, 0, 0))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.timeEdit_3 = QtWidgets.QTimeEdit(Searchlog_Dialog)
        self.timeEdit_3.setGeometry(QtCore.QRect(780, 320, 111, 31))
        self.timeEdit_3.setMaximumTime(QtCore.QTime(18, 59, 59))
        self.timeEdit_3.setMinimumTime(QtCore.QTime(13, 0, 0))
        self.timeEdit_3.setTime(QtCore.QTime(13, 30, 0))
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.timeEdit_4 = QtWidgets.QTimeEdit(Searchlog_Dialog)
        self.timeEdit_4.setGeometry(QtCore.QRect(930, 320, 111, 31))
        self.timeEdit_4.setMaximumTime(QtCore.QTime(18, 59, 59))
        self.timeEdit_4.setMinimumTime(QtCore.QTime(1, 0, 0))
        self.timeEdit_4.setTime(QtCore.QTime(15, 0, 0))
        self.timeEdit_4.setObjectName("timeEdit_4")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8 = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_8.setGeometry(QtCore.QRect(110, 350, 71, 31))
        self.label_8.setObjectName("label_8")
        self.label_lognum = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_lognum.setGeometry(QtCore.QRect(200, 350, 59, 31))
        self.label_lognum.setObjectName("label_lognum")
        self.label_lognum.setFont(font)
        self.label_10 = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_10.setGeometry(QtCore.QRect(360, 350, 91, 31))
        self.label_10.setObjectName("label_10")
        self.label_logacnum = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_logacnum.setGeometry(QtCore.QRect(480, 350, 59, 31))
        self.label_logacnum.setObjectName("label_logacnum")
        self.label_logacnum.setFont(font)
        self.label_9 = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_9.setGeometry(QtCore.QRect(900, 300, 31, 21))
        self.label_9.setObjectName("label_9")
        self.frame = QtWidgets.QFrame(Searchlog_Dialog)
        self.frame.setGeometry(QtCore.QRect(5, 420, 1081, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1081, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(Searchlog_Dialog)
        self.label_11.setGeometry(QtCore.QRect(10, 400, 71, 16))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Searchlog_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Searchlog_Dialog)

    def retranslateUi(self, Searchlog_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Searchlog_Dialog.setWindowTitle(_translate("Searchlog_Dialog", "用户管理"))
        self.label.setText(_translate("Searchlog_Dialog", "用户ID"))
        self.label_2.setText(_translate("Searchlog_Dialog", "用户姓名"))
        self.pushButton.setText(_translate("Searchlog_Dialog", "查询"))
        self.label_5.setText(_translate("Searchlog_Dialog", "考勤历史："))
        self.label_3.setText(_translate("Searchlog_Dialog", "日期范围"))
        self.label_4.setText(_translate("Searchlog_Dialog", "至"))
        self.label_6.setText(_translate("Searchlog_Dialog", "快速选择"))
        self.pushButton_preweek.setText(_translate("Searchlog_Dialog", "上一周"))
        self.pushButton_premonth.setText(_translate("Searchlog_Dialog", "上一月"))
        self.label_7.setText(_translate("Searchlog_Dialog", "时间范围"))
        self.label_8.setText(_translate("Searchlog_Dialog", "总考勤次数："))
        self.label_lognum.setText(_translate("Searchlog_Dialog", ""))
        self.label_10.setText(_translate("Searchlog_Dialog", "按时考勤次数："))
        self.label_logacnum.setText(_translate("Searchlog_Dialog", ""))
        self.label_9.setText(_translate("Searchlog_Dialog", "至"))
        self.label_11.setText(_translate("Searchlog_Dialog", "考勤曲线："))

