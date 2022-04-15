from PySide2 import QtWidgets

from ui.ui_abyss import Ui_Abyss


class AbyssWindow(QtWidgets.QMainWindow):
    def __init__(self, device):
        self.device = device
        super(AbyssWindow, self).__init__()
        self.ui = Ui_Abyss()
        self.ui.setupUi(self)

    def f_btn_download_daily_rom(self):
        pass

    def f_btn_download_output(self):
        pass