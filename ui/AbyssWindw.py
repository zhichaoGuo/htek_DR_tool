from threading import Thread

import yaml
from PySide2 import QtWidgets

from tool.HL_Signal import HlSignal
from tool.test_util import hl_request


class AbyssWindow(QtWidgets.QMainWindow):
    def __init__(self):
        from ui.ui_abyss import Ui_Abyss
        from tool.config import hlcfg
        super(AbyssWindow, self).__init__()
        self.ui = Ui_Abyss()
        self.ui.setupUi(self)
        # 创建信号
        self.HlSignal = HlSignal()
        try:
            self.ui.box_save_rom_path.addItems(hlcfg.get_option('save_rom_path'))
            self.ui.box_save_output_path.addItems(hlcfg.get_option('save_output_path'))
        except Exception:
            self.ui.box_save_rom_path.addItems(['C:/Users/admin'])
            self.ui.box_save_output_path.addItems(['C:/Users/admin'])
        self.HlSignal.show_message.connect(self._show_message)
        self.ui.btn_download_dailyt_rom.clicked.connect(self.f_btn_download_daily_rom)
        self.ui.btn_download_output.clicked.connect(self.f_btn_download_output)

    def f_btn_download_daily_rom(self):
        thread = Thread(target=download_daily_rom, args=[self, ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在telnet')

    def f_btn_download_output(self):
        thread = Thread(target=download_daily_rom, args=[self, ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在telnet')

    def show_message(self, message, level=0):
        self.HlSignal.show_message.emit(message, level)

    def _show_message(self, message, level=0):
        if level == 1:
            self.ui.label_info.setText(f'<font color=red>{message}</font>')
        else:
            self.ui.label_info.setText(message)
            self.ui.text_jenkins_url.text()
            self.ui.box_save_rom_path.currentText()

def download_daily_rom(window):
    window.ui.text_jenkins_url.text()
    save_path = window.ui.text_jenkins_url.text()
    url_frist = window.ui.box_save_rom_path.currentText()
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


def download_output(window):
    pass
