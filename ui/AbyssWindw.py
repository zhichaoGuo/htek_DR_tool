import datetime
import os
from threading import Thread
from PySide2 import QtWidgets

from tool.HL_Signal import HlSignal
from tool.abyss import AbyssInfo, less_info_device
from tool.test_util import hl_request

from PySide2.QtWidgets import *

all_header_checkbox = []


# 此为不可列不可编辑类
class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None


class AbyssWindow(QtWidgets.QMainWindow):
    def __init__(self):
        from PySide2.QtGui import QIcon
        from ui.ui_abyss import Ui_Abyss
        from tool.config import hlcfg
        super(AbyssWindow, self).__init__()
        self.ui = Ui_Abyss()
        self.ui.setupUi(self)
        # 创建并连接信号
        self.HlSignal = HlSignal()
        self.HlSignal.show_message.connect(self._show_message)
        # 设置配置中的文本
        self.ui.text_jenkins_url.setText(*hlcfg.get_option('download_daily_rom_url'))
        self.ui.text_output_path.setText(*hlcfg.get_option('download_output_url'))
        try:
            self.ui.box_save_rom_path.addItems(hlcfg.get_option('save_rom_path'))
            self.ui.box_save_output_path.addItems(hlcfg.get_option('save_output_path'))
        except Exception:
            self.ui.box_save_rom_path.addItems(['C:/Users/admin'])
            self.ui.box_save_output_path.addItems(['C:/Users/admin'])
        # 连接控件方法
        self.ui.btn_download_dailyt_rom.clicked.connect(self.f_btn_download_daily_rom)
        self.ui.btn_open_rom_dir.clicked.connect(self.f_btn_open_rom_dir)
        self.ui.btn_download_output.clicked.connect(self.f_btn_download_output)
        self.ui.btn_open_output_dir.clicked.connect(self.f_btn_open_output_dir)
        # 添加图标
        self.setWindowIcon(QIcon("htek.ico"))
        # 设置表格
        self.settable()

    def settable(self):
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        self.ui.tableWidget.setRowCount(15)  # 设置表格行数
        self.ui.tableWidget.setColumnWidth(0, 70)
        self.ui.tableWidget.setColumnWidth(1, 70)
        self.ui.tableWidget.setColumnWidth(2, 110)
        self.ui.tableWidget.setColumnWidth(3, 145)
        # 设置表格内容和复选框
        abyss_device = AbyssInfo()
        abyss_device = less_info_device(abyss_device.device)
        for i in range(len(abyss_device)):
            checkbox = QCheckBox()
            all_header_checkbox.append(checkbox)
            self.ui.tableWidget.setCellWidget(i, 0, checkbox)  # 设置表格可选项
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(f'   {abyss_device[i][0]}', text='model'))
            # 设置ip
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(abyss_device[i][1], text='ip'))
            # 设置mac
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(abyss_device[i][2], text='mac'))
            # 设置版本号
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(abyss_device[i][3], text='version'))
            # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 配置列不可编辑
        for i in [0, 1, 2, 3]:
            self.ui.tableWidget.setItemDelegateForColumn(i, EmptyDelegate(self.ui.tableWidget))

    # # 删除选中的行数
    # def delete_check(self):
    #     row_box_list = []
    #     # 获取选中数据
    #     for i in range(self.ui.tableWidget.rowCount()):
    #         if self.ui.tableWidget.cellWidget(i, 0).isChecked() is True:
    #             row_box_list.append(i)
    #             row_box_list.reverse()  # 将数据进行降序
    #     for j in row_box_list:
    #         self.ui.tableWidget.removeRow(j)  # 删除选中行数据
    #         all_header_checkbox.pop(j)  # 重新构建check box列表

    def f_btn_download_daily_rom(self):
        thread = Thread(target=download_daily_rom, args=[self, ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在下载rom')

    def f_btn_download_output(self):
        thread = Thread(target=download_output, args=[self, ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在下载output')

    def f_btn_open_rom_dir(self):
        start_directory = self.ui.box_save_rom_path.currentText()
        os.startfile(start_directory)

    def f_btn_open_output_dir(self):
        start_directory = self.ui.box_save_output_path.currentText()
        os.startfile(start_directory)

    def show_message(self, message, level=0):
        self.HlSignal.show_message.emit(message, level)

    def _show_message(self, message, level=0):
        if level == 1:
            self.ui.label_info.setText(f'<font color=red>{message}</font>')
        else:
            self.ui.label_info.setText(message)


def download_daily_rom(window):
    # url_frist 应为 http://repo.htek.com:8810/job/2.42.6.5.15R/ws/out/roms/neutral/
    from tool.config import hlcfg
    hlcfg.set_option('download_daily_rom_url', window.ui.text_jenkins_url.text())
    save_path = window.ui.box_save_rom_path.currentText()
    url_frist = window.ui.text_jenkins_url.text()
    rom_path_list = ['500M/fw500M.rom',
                     '520M/fw520M.rom',
                     '520U/fw520U.rom',
                     '900M/fw900M.rom',
                     '910M/fw910M.rom',
                     '920M/fw920M.rom',
                     '920U/fw920U.rom',
                     '930M/fw930M.rom']
    for rom_path in rom_path_list:
        url = url_frist + rom_path
        rom_name = rom_path[-10:]
        r = hl_request('GET', url)
        if r.status_code == 200:
            with open(save_path + rom_name, 'wb') as f:
                f.write(r.content)
            f.close()
        print(url)
    window.show_message('下载rom完成')


def download_output(window):
    # url_first 应为 http://abyss-dl.htek.com/.task/c6d9f29e-c06f-11ec-a693-000c29ffac12/output/
    from tool.config import hlcfg
    hlcfg.set_option('download_output_url', window.ui.text_output_path.text())
    url_first = window.ui.text_output_path.text()
    save_path = window.ui.box_save_output_path.currentText()
    save_path = save_path + '%s/' % str(datetime.date.today()).replace('-', '')
    r = hl_request('GET', url_first).text
    file_name_list = []
    import xml.etree.cElementTree as ET
    r = r.replace('</pre><hr>', '</pre></hr>')
    tree = ET.fromstring(r)
    # 设置下载文件名列表
    for i in range(len(list(tree[1][1][0])) - 1):
        file_name_list.append(list(tree[1][1][0])[i + 1].text)
    for file_name in file_name_list:
        url = url_first + file_name
        r = hl_request('GET', url)
        if r.status_code == 200:
            if not os.path.exists(save_path[:-1]):
                os.mkdir(save_path)
            with open(save_path + file_name, 'wb') as f:
                f.write(r.content)
            f.close()
        print(url)
    window.show_message('下载output完成')
