import yaml
from PySide2 import QtWidgets

from ui.ui_abyss import Ui_Abyss


class AbyssWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AbyssWindow, self).__init__()
        self.ui = Ui_Abyss()
        self.ui.setupUi(self)
        try:
            yaml.safe_load('abyss_cfg.yml')
        except Exception :
            pass
        self.ui.box_save_rom_path.addItems(['C:\\Users\\admin'])
        self.ui.box_save_output_path.addItems(['C:\\Users\\admin'])

    def f_btn_download_daily_rom(self):
        pass

    def f_btn_download_output(self):
        pass