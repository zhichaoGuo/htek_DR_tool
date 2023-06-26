from PySide2 import QtWidgets

from ui.ui_calllog import Ui_CalllogWindow


class CallLogWindow(QtWidgets.QMainWindow):
    def __init__(self, device):
        from PySide2.QtGui import QIcon
        self.device = device
        super(CallLogWindow, self).__init__()
        self.ui = Ui_CalllogWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("htek.ico"))  # 添加图标