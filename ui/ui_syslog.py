# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'syslog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SyslogWindow(object):
    def setupUi(self, SyslogWindow):
        if not SyslogWindow.objectName():
            SyslogWindow.setObjectName(u"SyslogWindow")
        SyslogWindow.resize(933, 449)
        self.centralwidget = QWidget(SyslogWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.syslog_text = QTextBrowser(self.centralwidget)
        self.syslog_text.setObjectName(u"syslog_text")
        self.syslog_text.setGeometry(QRect(10, 40, 911, 351))
        self.syslog_lab_title = QLabel(self.centralwidget)
        self.syslog_lab_title.setObjectName(u"syslog_lab_title")
        self.syslog_lab_title.setGeometry(QRect(260, 10, 121, 16))
        self.syslog_btn_copy = QPushButton(self.centralwidget)
        self.syslog_btn_copy.setObjectName(u"syslog_btn_copy")
        self.syslog_btn_copy.setGeometry(QRect(270, 400, 75, 23))
        self.syslog_btn_save = QPushButton(self.centralwidget)
        self.syslog_btn_save.setObjectName(u"syslog_btn_save")
        self.syslog_btn_save.setGeometry(QRect(390, 400, 75, 23))
        self.syslog_btn_open_in_txt = QPushButton(self.centralwidget)
        self.syslog_btn_open_in_txt.setObjectName(u"syslog_btn_open_in_txt")
        self.syslog_btn_open_in_txt.setGeometry(QRect(510, 400, 75, 23))
        self.syslog_lab_state = QLabel(self.centralwidget)
        self.syslog_lab_state.setObjectName(u"syslog_lab_state")
        self.syslog_lab_state.setGeometry(QRect(640, 410, 54, 12))
        SyslogWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SyslogWindow)
        self.statusbar.setObjectName(u"statusbar")
        SyslogWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SyslogWindow)

        QMetaObject.connectSlotsByName(SyslogWindow)
    # setupUi

    def retranslateUi(self, SyslogWindow):
        SyslogWindow.setWindowTitle(QCoreApplication.translate("SyslogWindow", u"HTT - syslog server", None))
        self.syslog_lab_title.setText(QCoreApplication.translate("SyslogWindow", u"TextLabel", None))
        self.syslog_btn_copy.setText(QCoreApplication.translate("SyslogWindow", u"\u5168\u90e8\u590d\u5236", None))
        self.syslog_btn_save.setText(QCoreApplication.translate("SyslogWindow", u"\u5168\u90e8\u4fdd\u5b58", None))
        self.syslog_btn_open_in_txt.setText(QCoreApplication.translate("SyslogWindow", u"\u5728TXT\u4e2d\u6253\u5f00", None))
        self.syslog_lab_state.setText(QCoreApplication.translate("SyslogWindow", u"\u72b6\u6001\u6b63\u5e38", None))
    # retranslateUi

