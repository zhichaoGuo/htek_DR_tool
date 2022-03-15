from PySide2 import QtCore
from PySide2.QtCore import Signal


class HlSignal(QtCore.QObject):
    # 定义信号
    print_syslog = Signal(str)
    download_syslog_over = Signal(str)
    save_file = Signal(str,bytes,str,str)
    def __init__(self):
        super(HlSignal, self).__init__()
