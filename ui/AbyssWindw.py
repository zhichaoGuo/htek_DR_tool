import datetime
import os
from threading import Thread
from PySide2 import QtWidgets

from tool.HL_Signal import HlSignal
from tool.test_util import hl_request


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
    hlcfg.set_option('download_daily_rom_url',window.ui.text_jenkins_url.text())
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
        r = hl_request('GET',url)
        if r.status_code ==200:
            with open(save_path+rom_name,'wb') as f:
                f.write(r.content)
            f.close()
        print(url)
    window.show_message('下载rom完成')


def download_output(window):
    # url_first 应为 http://abyss-dl.htek.com/.task/c6d9f29e-c06f-11ec-a693-000c29ffac12/output/
    from tool.config import hlcfg
    hlcfg.set_option('download_output_url',window.ui.text_output_path.text())
    url_first = window.ui.text_output_path.text()
    save_path = window.ui.box_save_output_path.currentText()
    save_path = save_path + '%s/' % str(datetime.date.today()).replace('-', '')
    r = hl_request('GET',url_first).text
    file_name_list = []
    import xml.etree.cElementTree as ET
    r = r.replace('</pre><hr>', '</pre></hr>')
    tree = ET.fromstring(r)
    # 设置下载文件名列表
    for i in range(len(list(tree[1][1][0])) - 1):
        file_name_list.append(list(tree[1][1][0])[i + 1].text)
    for file_name in file_name_list:
        url = url_first + file_name
        r = hl_request('GET',url)
        if r.status_code == 200:
            if not os.path.exists(save_path[:-1]):
                os.mkdir(save_path)
            with open(save_path + file_name, 'wb') as f:
                f.write(r.content)
            f.close()
        print(url)
    window.show_message('下载output完成')
