# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        if not TabWidget.objectName():
            TabWidget.setObjectName(u"TabWidget")
        TabWidget.resize(201, 700)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 191, 621))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 260, 171, 161))
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 40, 151, 20))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 120, 151, 23))
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 90, 151, 20))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 54, 12))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 54, 12))
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 171, 111))
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(62, 20, 101, 20))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 41, 16))
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 50, 151, 23))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 54, 12))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 90, 54, 12))
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 129, 171, 121))
        self.Btn_autotest = QPushButton(self.groupBox_3)
        self.Btn_autotest.setObjectName(u"Btn_autotest")
        self.Btn_autotest.setGeometry(QRect(10, 20, 75, 23))
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(90, 20, 75, 23))
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 50, 75, 23))
        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(90, 50, 75, 23))
        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 430, 171, 171))
        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 20, 71, 16))
        self.checkBox_2 = QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(90, 20, 71, 16))
        TabWidget.addTab(self.tab, "")

        self.retranslateUi(TabWidget)

        QMetaObject.connectSlotsByName(TabWidget)
    # setupUi

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(QCoreApplication.translate("TabWidget", u"TabWidget", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabWidget", u"\u5347\u7ea7", None))
        self.pushButton.setText(QCoreApplication.translate("TabWidget", u"AP", None))
        self.label_4.setText(QCoreApplication.translate("TabWidget", u"fw\u8def\u5f84", None))
        self.label_5.setText(QCoreApplication.translate("TabWidget", u"cfg\u8def\u5f84", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabWidget", u"\u8bbe\u5907\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("TabWidget", u"\u8bdd\u673aIP", None))
        self.pushButton_4.setText(QCoreApplication.translate("TabWidget", u"\u7ed1\u5b9a\u8bbe\u5907", None))
        self.label_2.setText(QCoreApplication.translate("TabWidget", u"\u8bbe\u5907\u72b6\u6001\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("TabWidget", u"\u672a\u7ed1\u5b9a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TabWidget", u"\u529f\u80fd\u533a", None))
        self.Btn_autotest.setText(QCoreApplication.translate("TabWidget", u"AutoTest", None))
        self.pushButton_3.setText(QCoreApplication.translate("TabWidget", u"\u8c03\u8bd5\u6a21\u5f0f", None))
        self.pushButton_5.setText(QCoreApplication.translate("TabWidget", u"\u91cd\u542f\u8bdd\u673a", None))
        self.pushButton_6.setText(QCoreApplication.translate("TabWidget", u"\u6062\u590d\u51fa\u5382", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TabWidget", u"\u6ce8\u518c\u4fe1\u606f", None))
        self.checkBox.setText(QCoreApplication.translate("TabWidget", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("TabWidget", u"CheckBox", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), QCoreApplication.translate("TabWidget", u"\u8bbe\u59071", None))
    # retranslateUi

