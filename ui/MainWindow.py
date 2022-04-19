from threading import Thread

from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide2.QtCore import Slot, QCoreApplication, Qt

from tool.HL_Signal import HlSignal
from tool.test_tool import set_pnum, set_pnums, save_screen, open_web, \
    save_syslog, save_xml_cfg, set_all_btn, WebImportRom, WebImportXmlCfg
from tool.test_util import isIPv4, isOnline, return_ip, save_file
from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        from tool.tag_page import Tag
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.WindowMinimizeButtonHint |  # 使能最小化按钮
                            Qt.WindowCloseButtonHint |  # 使能关闭按钮
                            Qt.WindowStaysOnTopHint)  # 窗体总在最前端
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("htek.ico"))
        # 分页
        self.D1 = Tag(self, 1)
        self.D2 = Tag(self, 2)
        self.D3 = Tag(self, 3)
        self.D4 = Tag(self, 4)
        # 按键加锁
        set_all_btn(self.D1, False)
        set_all_btn(self.D2, False)
        set_all_btn(self.D3, False)
        set_all_btn(self.D4, False)
        # 绑定按键回调函数
        self._connect_signal(self.D1)
        self._connect_signal(self.D2)
        self._connect_signal(self.D3)
        self._connect_signal(self.D4)
        self.btn_ABYSS.clicked.connect(self.f_btn_show_abyss)
        # 创建信号
        self.HlSignal = HlSignal()
        self.file = 'syslog'
        self.file_model = 'UC'
        self.file_methd = 'txt'
        self.HlSignal.save_file.connect(lambda: save_file(self, self.file, self.file_model, self.file_methd))
        self.HlSignal.show_message.connect(self._show_message)

    def closeEvent(self, event) -> None:
        from sys import exit
        exit(0)

    @Slot()
    def f_btn_band(self, tag):
        from tool.hl_device import VoipDevice
        """绑定设备，并解锁功能按钮"""
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
                # 查询并展示指派路径
                tag.refresh_state()
                tag.connect_state(True)
                self.show_message('绑定成功')
            # 设备在线但密码错误
            elif isOnline(tag.text_ip.text(), tag.box_password.currentText().split(':')[0],
                          tag.box_password.currentText().split(':')[1]) == 0:
                tag.connect_state(False)
                tag.lab_online.setText('<font color=red>█失败█</font>')
                self.show_message('绑定失败：密码错误', 1)
            # 设备离线
            else:
                tag.clean_state()
                tag.connect_state(False)
                self.show_message('绑定失败：设备无响应', 1)
        # ip 不为IPV4
        else:
            self.tabWidget.setTabText(self.tabWidget.indexOf(tag.tab),
                                      QCoreApplication.translate("MainWindow", "设备", None))
            tag.clean_state()
            tag.connect_state(False)
            QMessageBox.about(self, '登录提示', 'not ipv4')
            self.show_message('绑定失败：输入ip格式错误', 1)

    def f_btn_open_web(self, tag):
        """打开话机网页（不带验证）"""
        if open_web(tag.device):
            self.show_message('打开网页成功！')
        else:
            self.show_message('打开网页失败！', 1)

    def f_btn_autotest(self, tag):
        thread = Thread(target=tag.exec_autotest, args=[self, ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在autotest')

    def f_btn_telnet(self, tag):
        thread = Thread(target=tag.exec_telnet, args=[self, ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在telnet')

    def f_btn_reboot(self, tag):
        thread = Thread(target=tag.exec_reboot, args=[self, ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在reboot')

    def f_btn_factory(self, tag):
        thread = Thread(target=tag.exec_factory, args=[self, ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在恢复出厂')

    def f_btn_show_syslog(self, device, port: int):
        """打开syslog服务器并展示界面"""
        from ui.SysLogWindow import SyslogWindow
        # 配置syslog服务器
        set_pnum(device, 'P207', '%s:%s' % (return_ip(), str(port)))
        # 展示界面
        self.syslogwindow = SyslogWindow(device, port)
        self.syslogwindow.show()

    def f_btn_show_calllog(self, tag):
        """打开calllog界面"""
        from ui.CallLogWindow import CallLogWindow
        device = tag.device
        tag.calllogwindiw = CallLogWindow(device)
        tag.calllogwindiw.show()

    def f_btn_inport_rom(self, tag):
        from os.path import abspath
        rom_abspath = QFileDialog.getOpenFileName(self, '打开导入的rom', abspath('.'), '.rom(*.rom)')
        if rom_abspath[0] == '':
            return 0
        set_all_btn(tag, False)
        thread = Thread(target=WebImportRom, args=[self, tag, rom_abspath[0], ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在导入rom')

    def f_btn_inport_cfg(self, tag):
        from os.path import abspath
        rom_abspath = QFileDialog.getOpenFileName(self, '打开导入的xml', abspath('.'), '.xml(*.xml)')
        if rom_abspath[0] == '':
            return 0
        set_all_btn(tag, False)
        thread = Thread(target=WebImportXmlCfg, args=[self, tag, rom_abspath[0], ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在导入xml')

    def f_btn_ap(self, tag):
        thread = Thread(target=tag.exec_ap, args=[self, ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在ap')

    def f_btn_pslect(self, tag):
        thread = Thread(target=tag.exec_select_p, args=[self, ])
        thread.setDaemon(True)
        thread.start()
        self.show_message('正在slect P值')

    def f_btn_pset(self, tag):
        if tag.text_pnum.text() == '':
            QMessageBox.about(self, '提示', 'P值不能为空')
        else:
            ret = set_pnum(tag.device, 'P' + tag.text_pnum.text(), tag.text_pvalue.text())
            tag.refresh_state()
            if ret is False:
                QMessageBox.about(self, '提示', 'P值设置失败')

    def f_btn_register(self, tag):
        """注册选中的注册信息"""
        from yaml import safe_load
        from tool.config import hlcfg
        current_account ={}
        for data in hlcfg.get_option('register_date'):
            if tag.box_register.currentText() in data.keys():
                current_account = data[tag.box_register.currentText()]
                break
        if current_account is  not None:
            sip_server = current_account['sip_server']
            sip_user = current_account['sip_user']
            Authenticate = current_account['Authenticate']
            sip_password = current_account['sip_password']
            set_dic = {'P47': sip_server,  # sip server
                       'P480': '',  # outbound server
                       'P130': '0',  # SIP Transport
                       'P271': '1',  # account active
                       'P24082': '0',  # Profile 1
                       'P35': sip_user,  # SIP User ID
                       'P36': Authenticate,  # Authenticate ID
                       'P34': sip_password}  # Authenticate Password
            set_pnums(tag.device, set_dic)

    def f_btn_reset_account(self, tag):
        """为当前话机去注册"""
        set_dic = {'P47': '',  # sip server
                   'P480': '',  # outbound server
                   'P130': '0',  # SIP Transport
                   'P271': '0',  # account active
                   'P24082': '0',  # Profile 1
                   'P35': '',  # SIP User ID
                   'P36': '',  # Authenticate ID
                   'P34': ''}  # Authenticate Password
        set_pnums(tag.device, set_dic)

    def f_btn_save_screen(self, tag):
        """保存截图"""
        # 起新线程下载syslog
        thread = Thread(target=save_screen, args=[self, tag.device, ])
        # 设置成守护线程
        thread.setDaemon(True)
        # 启动线程
        thread.start()
        self.show_message('正在保存截图')

    def f_btn_save_syslog(self, tag):
        """保存话机日志"""
        # 起新线程下载syslog
        thread = Thread(target=save_syslog, args=[self, tag.device, ])
        # 设置成守护线程
        thread.setDaemon(True)
        # 启动线程
        thread.start()
        self.show_message('正在保存日志')

    def f_btn_save_cfg(self, tag):
        """保存话机xml配置"""
        # 起新线程下载syslog
        thread = Thread(target=save_xml_cfg, args=[self, tag.device, ])
        # 设置成守护线程
        thread.setDaemon(True)
        # 启动线程
        thread.start()
        self.show_message('正在保存配置')

    def f_btn_open_ptxt(self):
        """打开话机P值表"""
        from os import system
        thread = Thread(target=system, args=["notepad.exe P值表.txt", ])
        thread.setDaemon(True)
        thread.start()

    def f_btn_show_abyss(self):
        """打开abyss并展示界面"""
        from ui.AbyssWindw import AbyssWindow
        # 展示界面
        self.abysswindow = AbyssWindow()
        self.abysswindow.show()

    def _connect_signal(self, tag):
        tag.btn_band.clicked.connect(lambda: self.f_btn_band(tag))
        tag.btn_web.clicked.connect(lambda: self.f_btn_open_web(tag))
        tag.btn_autotest.clicked.connect(lambda: self.f_btn_autotest(tag))
        tag.btn_telnet.clicked.connect(lambda: self.f_btn_telnet(tag))
        tag.btn_reboot.clicked.connect(lambda: self.f_btn_reboot(tag))
        tag.btn_factory.clicked.connect(lambda: self.f_btn_factory(tag))
        tag.btn_logserver.clicked.connect(lambda: self.f_btn_show_syslog(tag.device, tag.logserver_port))
        tag.btn_calllog.clicked.connect(lambda: self.f_btn_show_calllog(tag))
        tag.btn_inport_rom.clicked.connect(lambda: self.f_btn_inport_rom(tag))
        tag.btn_inport_cfg.clicked.connect(lambda: self.f_btn_inport_cfg(tag))
        tag.btn_ap.clicked.connect(lambda: self.f_btn_ap(tag))
        tag.btn_pselect.clicked.connect(lambda: self.f_btn_pslect(tag))
        tag.btn_ptxt.clicked.connect(lambda: self.f_btn_open_ptxt())
        tag.btn_pset.clicked.connect(lambda: self.f_btn_pset(tag))
        tag.btn_register.clicked.connect(lambda: self.f_btn_register(tag))
        tag.btn_reset_account.clicked.connect(lambda: self.f_btn_reset_account(tag))
        tag.btn_savescreen.clicked.connect(lambda: self.f_btn_save_screen(tag))
        tag.btn_savelog.clicked.connect(lambda: self.f_btn_save_syslog(tag))
        tag.btn_savecfg.clicked.connect(lambda: self.f_btn_save_cfg(tag))

    def show_message(self, message, level=0):
        self.HlSignal.show_message.emit(message, level)

    def _show_message(self, message, level=0):
        if level == 1:
            self.label_9.setText(f'<font color=red>{message}</font>')
        else:
            self.label_9.setText(message)
