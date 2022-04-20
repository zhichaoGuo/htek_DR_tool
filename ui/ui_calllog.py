# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calllog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CalllogWindow(object):
    def setupUi(self, CalllogWindow):
        if not CalllogWindow.objectName():
            CalllogWindow.setObjectName(u"CalllogWindow")
        CalllogWindow.resize(407, 300)
        self.groupBox = QGroupBox(CalllogWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 161, 281))
        self.calllog_text = QTextBrowser(self.groupBox)
        self.calllog_text.setObjectName(u"calllog_text")
        self.calllog_text.setGeometry(QRect(10, 20, 141, 251))
        self.groupBox_2 = QGroupBox(CalllogWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(180, 10, 221, 211))
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 40, 51, 20))
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 40, 61, 20))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 54, 12))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 20, 54, 12))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 20, 54, 12))
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(140, 40, 69, 22))
        self.groupBox_3 = QGroupBox(CalllogWindow)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(180, 230, 221, 61))

        self.retranslateUi(CalllogWindow)

        QMetaObject.connectSlotsByName(CalllogWindow)
    # setupUi

    def retranslateUi(self, CalllogWindow):
        CalllogWindow.setWindowTitle(QCoreApplication.translate("CalllogWindow", u"HTT - Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("CalllogWindow", u"\u9884\u89c8\u533a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("CalllogWindow", u"\u5bfc\u5165\u533a", None))
        self.label.setText(QCoreApplication.translate("CalllogWindow", u"\u8bb0\u5f55\u59d3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("CalllogWindow", u"\u53f7\u7801", None))
        self.label_3.setText(QCoreApplication.translate("CalllogWindow", u"\u8bb0\u5f55\u7c7b\u578b", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("CalllogWindow", u"\u5bfc\u51fa\u533a", None))
    # retranslateUi

