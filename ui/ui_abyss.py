# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'abyss.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Abyss(object):
    def setupUi(self, Abyss):
        if not Abyss.objectName():
            Abyss.setObjectName(u"Abyss")
        Abyss.resize(1113, 684)
        self.tableWidget = QTableWidget(Abyss)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 691, 661))
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.btn_refresh = QPushButton(Abyss)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(710, 10, 121, 31))
        self.groupBox = QGroupBox(Abyss)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(710, 50, 391, 81))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 71, 22))
        self.text_jenkins_url = QLineEdit(self.groupBox)
        self.text_jenkins_url.setObjectName(u"text_jenkins_url")
        self.text_jenkins_url.setGeometry(QRect(80, 20, 301, 20))
        self.box_save_rom_path = QComboBox(self.groupBox)
        self.box_save_rom_path.setObjectName(u"box_save_rom_path")
        self.box_save_rom_path.setGeometry(QRect(80, 50, 181, 22))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 54, 22))
        self.btn_download_dailyt_rom = QPushButton(self.groupBox)
        self.btn_download_dailyt_rom.setObjectName(u"btn_download_dailyt_rom")
        self.btn_download_dailyt_rom.setGeometry(QRect(270, 50, 61, 23))
        self.btn_open_rom_dir = QPushButton(self.groupBox)
        self.btn_open_rom_dir.setObjectName(u"btn_open_rom_dir")
        self.btn_open_rom_dir.setGeometry(QRect(340, 50, 41, 23))
        self.groupBox_2 = QGroupBox(Abyss)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(710, 140, 391, 80))
        self.text_output_path = QLineEdit(self.groupBox_2)
        self.text_output_path.setObjectName(u"text_output_path")
        self.text_output_path.setGeometry(QRect(80, 20, 301, 20))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 71, 22))
        self.box_save_output_path = QComboBox(self.groupBox_2)
        self.box_save_output_path.setObjectName(u"box_save_output_path")
        self.box_save_output_path.setGeometry(QRect(80, 50, 181, 22))
        self.btn_download_output = QPushButton(self.groupBox_2)
        self.btn_download_output.setObjectName(u"btn_download_output")
        self.btn_download_output.setGeometry(QRect(270, 50, 61, 23))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 50, 54, 22))
        self.btn_open_output_dir = QPushButton(self.groupBox_2)
        self.btn_open_output_dir.setObjectName(u"btn_open_output_dir")
        self.btn_open_output_dir.setGeometry(QRect(340, 50, 41, 23))
        self.label_info = QLabel(Abyss)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(860, 20, 241, 16))
        self.groupBox_3 = QGroupBox(Abyss)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(710, 230, 391, 141))
        self.text_abyss_upgrade_url = QLineEdit(self.groupBox_3)
        self.text_abyss_upgrade_url.setObjectName(u"text_abyss_upgrade_url")
        self.text_abyss_upgrade_url.setGeometry(QRect(80, 20, 251, 20))
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 71, 22))
        self.btn_abyss_upgrade = QPushButton(self.groupBox_3)
        self.btn_abyss_upgrade.setObjectName(u"btn_abyss_upgrade")
        self.btn_abyss_upgrade.setGeometry(QRect(340, 20, 41, 23))
        self.btn_abyss_factory = QPushButton(self.groupBox_3)
        self.btn_abyss_factory.setObjectName(u"btn_abyss_factory")
        self.btn_abyss_factory.setGeometry(QRect(80, 50, 61, 23))
        self.btn_abyss_reboot = QPushButton(self.groupBox_3)
        self.btn_abyss_reboot.setObjectName(u"btn_abyss_reboot")
        self.btn_abyss_reboot.setGeometry(QRect(150, 50, 61, 23))

        self.retranslateUi(Abyss)

        QMetaObject.connectSlotsByName(Abyss)
    # setupUi

    def retranslateUi(self, Abyss):
        Abyss.setWindowTitle(QCoreApplication.translate("Abyss", u"HTT - abyss", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Abyss", u"\u578b\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Abyss", u"ip", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Abyss", u"mac", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Abyss", u"\u7248\u672c\u53f7", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Abyss", u"app", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Abyss", u"state", None));
        self.btn_refresh.setText(QCoreApplication.translate("Abyss", u"\u5237\u65b0", None))
        self.groupBox.setTitle(QCoreApplication.translate("Abyss", u"daily rom \u4e0b\u8f7d", None))
        self.label.setText(QCoreApplication.translate("Abyss", u"jenkins url", None))
        self.label_2.setText(QCoreApplication.translate("Abyss", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.btn_download_dailyt_rom.setText(QCoreApplication.translate("Abyss", u"\u5f00\u59cb\u4e0b\u8f7d", None))
        self.btn_open_rom_dir.setText(QCoreApplication.translate("Abyss", u"\u6253\u5f00", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Abyss", u"task\\output \u6570\u636e\u4e0b\u8f7d", None))
        self.label_3.setText(QCoreApplication.translate("Abyss", u"output\u8def\u5f84", None))
        self.btn_download_output.setText(QCoreApplication.translate("Abyss", u"\u5f00\u59cb\u4e0b\u8f7d", None))
        self.label_4.setText(QCoreApplication.translate("Abyss", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.btn_open_output_dir.setText(QCoreApplication.translate("Abyss", u"\u6253\u5f00", None))
        self.label_info.setText(QCoreApplication.translate("Abyss", u"\u63d0\u793a\u4fe1\u606f\u5728\u6b64\u663e\u793a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Abyss", u"abyss\u6279\u91cf\u64cd\u4f5c", None))
        self.label_5.setText(QCoreApplication.translate("Abyss", u"   \u5347\u7ea7url", None))
        self.btn_abyss_upgrade.setText(QCoreApplication.translate("Abyss", u"\u5347\u7ea7", None))
        self.btn_abyss_factory.setText(QCoreApplication.translate("Abyss", u"\u6062\u590d\u51fa\u5382", None))
        self.btn_abyss_reboot.setText(QCoreApplication.translate("Abyss", u"\u91cd\u542f", None))
    # retranslateUi

