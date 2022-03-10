from socket import socket,AF_INET,SOCK_DGRAM,SOL_SOCKET,SO_REUSEADDR
from threading import Thread

from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Signal

from tool.test_tool import set_pnum
from tool.test_util import return_ip
from ui.ui_syslog import Ui_SyslogWindow


class SyslogWindow(QtWidgets.QMainWindow):
    def __init__(self, device, port: int):
        self.device = device
        super(SyslogWindow, self).__init__()
        self.s = socket(AF_INET, SOCK_DGRAM)
        # 进行socekt配置，使其支持端口复用，否则发送方绑定5066，则无法使用该端口进行接收
        self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.s.setblocking(True)
        self.s.bind((return_ip(), port))
        # 创建线程用于自动回应注册包
        thread = Thread(target=self.child_thread, args=[self.s, ])
        # 设置成守护线程
        thread.setDaemon(True)
        # 启动线程
        thread.start()
        self.ui = Ui_SyslogWindow()
        self.ui.setupUi(self)
        self.LSignal = LogSignal()
        self.text = 'syslog'
        self.LSignal.print_syslog.connect(
            lambda: self.update_sysylog(self.text[22:-1].replace("\\n\\x00", "").replace(" : ", ":")))

    def update_sysylog(self, text: str):
        self.ui.syslog_text.append(text)

    def child_thread(self, s: socket):
        try:
            while True:
                buf, (dut_ip, dut_port) = s.recvfrom(1500)
                self.text = str(buf)
                self.LSignal.print_syslog.emit(self.text)
        except OSError as err:
            print(err)

    def closeEvent(self, event) -> None:
        set_pnum(self.device, 'P207', '')
        self.s.close()


class LogSignal(QtCore.QObject):
    # 定义信号
    print_syslog = Signal(str)

    def __init__(self):
        super(LogSignal, self).__init__()