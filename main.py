import datetime
import os
import sys
import socket
from threading import Thread

import yaml
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QFileDialog

from hl_device import VoipDevice

from test_tool import query_pnum, set_pnum, AutoProvisionNow, skip_rom_check, set_pnums, save_screen
from test_util import isIPv4, request, isOnline, return_ip
from ui_main import Ui_MainWindow
from PySide2.QtCore import Slot, QCoreApplication, Signal

from ui_syslog import Ui_SyslogWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        from tag_page import Tag
        super(MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |  # 使能最小化按钮
                            QtCore.Qt.WindowCloseButtonHint |  # 使能关闭按钮
                            QtCore.Qt.WindowStaysOnTopHint)  # 窗体总在最前端
        self.setupUi(self)
        self.D1 = Tag(self, 1)
        self.set_all_btn(self.D1, False)  # 按键加锁
        # 页面分类
        # self._set_tag()
        # 绑定按键回调函数
        self._connect_signal(self.D1)

    def closeEvent(self, event) -> None:
        sys.exit(0)

    @Slot()
    def f_btn_band(self, tag):
        # 检查ip合法性
        if isIPv4(tag.text_ip.text()):
            # 检查设备是否在线
            if isOnline(tag.text_ip.text(), tag.box_password.currentText().split(':')[0],
                        tag.box_password.currentText().split(':')[1]) == 1:
                # 生成设备对象包含ip mac version user password model
                tag.device = VoipDevice(tag.text_ip.text(), tag.box_password.currentText().split(':')[0],
                                        tag.box_password.currentText().split(':')[1])
                # 设置页签为model（型号）
                self.tabWidget.setTabText(self.tabWidget.indexOf(tag.tab),
                                          QCoreApplication.translate("MainWindow", tag.device.model, None))
                self.set_all_btn(tag, True)  # 解锁页面btn
                tag.text_fw.setText(query_pnum(tag.device, '192'))
                tag.text_cfg.setText(query_pnum(tag.device, '237'))
                tag.lab_online.setText('<font color=green>█在线█</font>')
                QMessageBox.about(self, '登录提示', tag.device.user + '绑定成功' + tag.device.model)
            # 设备在线但密码错误
            elif isOnline(tag.text_ip.text(), tag.box_password.currentText().split(':')[0],
                          tag.box_password.currentText().split(':')[1]) == 0:
                tag.lab_online.setText('<font color=red>█失败█</font>')
                self.set_all_btn(tag, False)
                QMessageBox.about(self, '登录提示', '密码错误')
            # 设备离线
            else:
                tag.lab_online.setText('<font color=red>█离线█</font>')
                self.set_all_btn(tag, False)
                QMessageBox.about(self, '登录提示', '无响应')
        else:
            self.tabWidget.setTabText(self.tabWidget.indexOf(tag.tab),
                                      QCoreApplication.translate("MainWindow", "设备", None))
            QMessageBox.about(self, '登录提示', 'not ipv4')

    def f_btn_autotest(self, device):
        url = 'http://%s/enable_autotest_api' % device.ip
        r = request('GET', url, auth=(device.user, device.password))
        if r.status_code != 200:
            QMessageBox.about(self, '登录提示', 'enable_autotest失败')

    def f_btn_telnet(self, device):
        self.f_btn_autotest(device)
        url1 = 'http://%s/AutoTest&action=enabletelnet' % device.ip
        r = request('GET', url1, auth=(device.user, device.password))
        if r.status_code != 200:
            QMessageBox.about(self, '登录提示', 'enable telnet失败')
        url2 = 'http://%s/AutoTest&action=enableftp' % device.ip
        r = request('GET', url2, auth=(device.user, device.password))
        if r.status_code != 200:
            QMessageBox.about(self, '登录提示', 'enable ftp失败')

    def f_btn_reboot(self, device):
        url = 'http://%s/rb_phone.htm' % device.ip
        r = request('GET', url, auth=(device.user, device.password))
        if r.status_code != 200:
            QMessageBox.about(self, '登录提示', 'reboot失败')

    def f_btn_factory(self, device):
        self.f_btn_autotest(device)
        url = 'http://%s/Abyss/FactoryReset' % device.ip
        r = request('GET', url, auth=(device.user, device.password))
        if r.status_code != 200:
            QMessageBox.about(self, '登录提示', 'reset factory失败')

    def f_btn_show_syslog(self, device, port: int):
        set_pnum(device, 'P207', '%s:%s' % (return_ip(), str(port)))
        self.syslogwindow = SyslogWindow(device, port)
        self.syslogwindow.show()

    def f_btn_ap(self, tag):
        skip_rom_check(tag.device)
        set_pnum(tag.device, 'P192', tag.text_fw.text())
        set_pnum(tag.device, 'P237', tag.text_cfg.text())
        AutoProvisionNow(tag.device)

    def f_btn_pslect(self, tag):
        if tag.text_pnum.text() == '':
            tag.text_pvalue.setText('')
        else:
            tag.text_pvalue.setText(query_pnum(tag.device, str(tag.text_pnum.text())))

    def f_btn_pset(self, tag):
        if tag.text_pnum.text() == '':
            QMessageBox.about(self, '提示', 'P值不能为空')
        else:
            ret = set_pnum(tag.device, 'P' + tag.text_pnum.text(), tag.text_pvalue.text())
            if not ret:
                QMessageBox.about(self, '提示', 'P值设置失败')

    def f_btn_register(self, tag):
        current_account = yaml.safe_load(open('register_date.yml', 'r', encoding='utf-8').read())[
            tag.box_register.currentText()]
        sip_server = current_account['sip_server']
        sip_user = current_account['sip_user']
        sip_password = current_account['sip_password']
        set_dic = {'P47': sip_server,  # sip server
                   'P480': '',  # outbound server
                   'P130': '0',  # SIP Transport
                   'P271': '1',  # account active
                   'P24082': '0',  # Profile 1
                   'P35': sip_user,  # SIP User ID
                   'P36': sip_user,  # Authenticate ID
                   'P34': sip_password}  # Authenticate Password
        set_pnums(tag.device, set_dic)

    def f_btn_save_screen(self, tag):
        pic_data = save_screen(tag.device)
        file_name = '[' + str(datetime.datetime.now())[5:].replace(":", "·").replace("-", "").split(".")[0].replace(" ",
                                                                                                                    "]")
        file_name = file_name.split(']')[0] + f'][{tag.device.model}]' + file_name.split(']')[1]
        filePath = QFileDialog.getSaveFileName(self, '保存路径', f'{os.path.abspath(".")}\\screen\\{file_name}.bmp',
                                               '.bmp(*.bmp)')
        with open(filePath[0], "wb") as f:
            f.write(pic_data)
        f.close()

    def f_btn_save_syslog(self, device):
        pass

    def f_btn_save_cfg(self, device):
        pass

    def set_all_btn(self, tag, value):
        if value in [True, False]:
            tag.btn_autotest.setEnabled(value)
            tag.btn_telnet.setEnabled(value)
            tag.btn_reboot.setEnabled(value)
            tag.btn_factory.setEnabled(value)
            tag.btn_ap.setEnabled(value)
            tag.btn_pselect.setEnabled(value)
            tag.btn_pset.setEnabled(value)
            tag.btn_logserver.setEnabled(value)
            tag.btn_register.setEnabled(value)
            tag.btn_savescreen.setEnabled(value)
            tag.btn_savelog.setEnabled(value)
            tag.btn_savecfg.setEnabled(value)

    def _connect_signal(self, tag):
        tag.btn_band.clicked.connect(lambda: self.f_btn_band(tag))
        tag.btn_autotest.clicked.connect(lambda: self.f_btn_autotest(tag.device))
        tag.btn_telnet.clicked.connect(lambda: self.f_btn_telnet(tag.device))
        tag.btn_reboot.clicked.connect(lambda: self.f_btn_reboot(tag.device))
        tag.btn_factory.clicked.connect(lambda: self.f_btn_factory(tag.device))
        tag.btn_logserver.clicked.connect(lambda: self.f_btn_show_syslog(tag.device, 5129))
        tag.btn_ap.clicked.connect(lambda: self.f_btn_ap(tag))
        tag.btn_pselect.clicked.connect(lambda: self.f_btn_pslect(tag))
        tag.btn_pset.clicked.connect(lambda: self.f_btn_pset(tag))
        tag.btn_register.clicked.connect(lambda: self.f_btn_register(tag))
        tag.btn_savescreen.clicked.connect(lambda: self.f_btn_save_screen(tag))

    def show_message(self, message, level=0):
        if level == 1:
            self.lab_message.setText(f'<font color=red>{message}</font>')
        else:
            self.lab_message.setText(message)


class SyslogWindow(QtWidgets.QMainWindow):
    def __init__(self, device, port: int):
        self.device = device
        super(SyslogWindow, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 进行socekt配置，使其支持端口复用，否则发送方绑定5066，则无法使用该端口进行接收
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())
