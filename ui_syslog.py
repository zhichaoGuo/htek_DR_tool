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
        SyslogWindow.resize(750, 449)
        self.centralwidget = QWidget(SyslogWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.syslog_text = QTextBrowser(self.centralwidget)
        self.syslog_text.setObjectName(u"syslog_text")
        self.syslog_text.setGeometry(QRect(10, 40, 731, 351))
        self.syslog_lab = QLabel(self.centralwidget)
        self.syslog_lab.setObjectName(u"syslog_lab")
        self.syslog_lab.setGeometry(QRect(260, 10, 121, 16))
        self.syslog_btn_copy = QPushButton(self.centralwidget)
        self.syslog_btn_copy.setObjectName(u"syslog_btn_copy")
        self.syslog_btn_copy.setGeometry(QRect(270, 400, 75, 23))
        SyslogWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SyslogWindow)
        self.statusbar.setObjectName(u"statusbar")
        SyslogWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SyslogWindow)

        QMetaObject.connectSlotsByName(SyslogWindow)
    # setupUi

    def retranslateUi(self, SyslogWindow):
        SyslogWindow.setWindowTitle(QCoreApplication.translate("SyslogWindow", u"MainWindow", None))
        self.syslog_lab.setText(QCoreApplication.translate("SyslogWindow", u"TextLabel", None))
        self.syslog_btn_copy.setText(QCoreApplication.translate("SyslogWindow", u"PushButton", None))
    # retranslateUi

