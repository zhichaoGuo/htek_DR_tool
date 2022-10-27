from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread

from pyperclip import copy
from PySide2 import QtWidgets

from tool.HL_Signal import HlSignal
from tool.test_tool import set_pnum
from tool.test_util import return_ip, save_file
from ui.ui_syslog import Ui_SyslogWindow


class SyslogWindow(QtWidgets.QMainWindow):
    def __init__(self, device, port: int):  # 添加图标
        self.device = device
        super(SyslogWindow, self).__init__()
        self.s = socket(AF_INET, SOCK_DGRAM)
        # 进行socekt配置，使其支持端口复用，否则发送方绑定5066，则无法使用该端口进行接收
        self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.s.setblocking(True)
        self.s.bind((return_ip(), port))
        self.ui = Ui_SyslogWindow()
        self.ui.setupUi(self)
        self.LSignal = HlSignal()
        self.text = 'syslog'
        self.LSignal.print_syslog.connect(
            lambda: self.update_sysylog(self.text[22:-1].replace("\\n\\x00", "").replace(" : ", ":")))
        # 创建线程
        thread = Thread(target=self.child_thread, args=[self.s, ])
        # 设置成守护线程
        thread.setDaemon(True)
        # 启动线程
        thread.start()
        self.ui.syslog_btn_copy.clicked.connect(self.f_btn_copy_all)
        self.ui.syslog_btn_save.clicked.connect(self.f_btn_save_log)
        self.ui.syslog_btn_open_in_txt.clicked.connect(lambda: self.f_btn_open_in_notepad())
        from PySide2.QtGui import QIcon
        self.setWindowIcon(QIcon("htek.ico"))

    def f_btn_copy_all(self):
        print('copy all syslog')
        copy(self.ui.syslog_text.document().toPlainText())

    def f_btn_save_log(self):
        file_buf = bytes(self.ui.syslog_text.document().toPlainText(),encoding = 'utf-8')
        file_path = save_file(self, file_buf, self.device.model, 'txt' )
        return file_path

    def f_btn_open_in_notepad(self):
        try:
            file_path = self.f_btn_save_log()
        except TypeError:
            return False

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

    def show_message(self, message, level=0):
        if level == 1:
            self.ui.syslog_lab_state.setText(f'<font color=red>{message}</font>')
        else:
            self.ui.syslog_lab_state.setText(message)