import webbrowser
from datetime import datetime
from os.path import abspath
import sys
from threading import Thread

from yaml import safe_load
from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide2.QtCore import Slot, QCoreApplication,Qt

from tool.HL_Signal import HlSignal
from tool.hl_device import VoipDevice
from tool.test_tool import query_pnum, set_pnum, AutoProvisionNow, skip_rom_check, set_pnums, save_screen, open_web, \
    save_syslog, save_xml_cfg
from tool.test_util import isIPv4, hl_request, isOnline, return_ip, save_file
from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        from tool.tag_page import Tag
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.WindowMinimizeButtonHint |  # 使能最小化按钮
                            Qt.WindowCloseButtonHint |  # 使能关闭按钮
                            Qt.WindowStaysOnTopHint)  # 窗体总在最前端
        self.setupUi(self)
        # 分页
        self.D1 = Tag(self, 1)
        self.D2 = Tag(self, 2)
        self.D3 = Tag(self, 3)
        self.D4 = Tag(self, 4)
        # 按键加锁
        self.set_all_btn(self.D1, False)
        self.set_all_btn(self.D2, False)
        self.set_all_btn(self.D3, False)
        self.set_all_btn(self.D4, False)
        # 绑定按键回调函数
        self._connect_signal(self.D1)
        self._connect_signal(self.D2)
        self._connect_signal(self.D3)
        self._connect_signal(self.D4)
        # 创建信号
        self.HlSignal = HlSignal()
        self.file = 'syslog'
        self.file_model = 'UC'
        self.file_methd = 'txt'
        self.HlSignal.save_file.connect(
            lambda: save_file(self,self.file,self.file_model,self.file_methd))

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
                # 查询并展示指派路径
                tag.text_fw.setText(query_pnum(tag.device, '192'))
                tag.text_cfg.setText(query_pnum(tag.device, '237'))
                # 更新状态，展示提示框
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
        """执行 enable_autotest_api"""
        url = 'http://%s/enable_autotest_api' % device.ip
        r = hl_request('GET', url, auth=(device.user, device.password))
        if r.status_code != 200:
            QMessageBox.about(self, '登录提示', 'enable_autotest失败')

    def f_btn_telnet(self, device):
        """执行 enable telnet 和 enable ftp"""
        self.f_btn_autotest(device)
        url1 = 'http://%s/AutoTest&action=enabletelnet' % device.ip
        r = hl_request('GET', url1, auth=(device.user, device.password))
        if r.status_code != 200:
            QMessageBox.about(self, '登录提示', 'enable telnet失败')
        url2 = 'http://%s/AutoTest&action=enableftp' % device.ip
        r = hl_request('GET', url2, auth=(device.user, device.password))
        if r.status_code != 200:
            QMessageBox.about(self, '登录提示', 'enable ftp失败')

    def f_btn_reboot(self, device):
        """重启话机"""
        url = 'http://%s/rb_phone.htm' % device.ip
        r = hl_request('GET', url, auth=(device.user, device.password))
        if r.status_code != 200:
            QMessageBox.about(self, '登录提示', 'reboot失败')

    def f_btn_factory(self, device):
        """恢复出厂"""
        self.f_btn_autotest(device)
        url = 'http://%s/Abyss/FactoryReset' % device.ip
        r = hl_request('GET', url, auth=(device.user, device.password))
        if r.status_code != 200:
            QMessageBox.about(self, '登录提示', 'reset factory失败')

    def f_btn_show_syslog(self, device, port: int):
        """打开syslog服务器并展示界面"""
        from ui.SysLogWindow import SyslogWindow
        # 配置syslog服务器
        set_pnum(device, 'P207', '%s:%s' % (return_ip(), str(port)))
        # 展示界面
        self.syslogwindow = SyslogWindow(device, port)
        self.syslogwindow.show()

    def f_btn_ap(self, tag):
        """设置fw和cfg地址并执行skip rom check"""
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
        current_account = safe_load(open('register_date.yml', 'r', encoding='utf-8').read())[tag.box_register.currentText()]
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
        # 起新线程下载syslog
        thread = Thread(target=save_screen, args=[self, tag.device, ])
        # 设置成守护线程
        thread.setDaemon(True)
        # 启动线程
        thread.start()

    def f_btn_save_syslog(self, tag):
        # 起新线程下载syslog
        thread = Thread(target=save_syslog, args=[self,tag.device, ])
        # 设置成守护线程
        thread.setDaemon(True)
        # 启动线程
        thread.start()

    def f_btn_save_cfg(self, tag):
        # 起新线程下载syslog
        thread = Thread(target=save_xml_cfg, args=[self, tag.device, ])
        # 设置成守护线程
        thread.setDaemon(True)
        # 启动线程
        thread.start()

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
        tag.btn_savelog.clicked.connect(lambda: self.f_btn_save_syslog(tag))
        tag.btn_savecfg.clicked.connect(lambda: self.f_btn_save_cfg(tag))

    def show_message(self, message, level=0):
        if level == 1:
            self.lab_message.setText(f'<font color=red>{message}</font>')
        else:
            self.lab_message.setText(message)


