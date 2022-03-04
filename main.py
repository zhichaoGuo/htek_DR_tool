import sys

from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

from hl_device import VoipDevice
from test_tool import query_pnum, set_pnum, AutoProvisionNow, skip_rom_check
from test_util import isIPv4, request, isOnline
from ui_main import Ui_MainWindow
from PySide2.QtCore import Slot, QCoreApplication


class MainWindow(QMainWindow, Ui_MainWindow):
    D1_ip = ''
    D1_name = ''
    D1_password = ''
    D2_ip = ''
    D2_name = ''
    D2_password = ''

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |  # 使能最小化按钮
                            QtCore.Qt.WindowCloseButtonHint |  # 使能关闭按钮
                            QtCore.Qt.WindowStaysOnTopHint)  # 窗体总在最前端
        self.setupUi(self)
        # 按键加锁
        self.set_all_btn(1, False)
        # 添加密码选项内容
        self.D1_box_password.addItems(['admin:admin', 'Administrator:9102SerCloudPBX', 'user:1234'])
        self.D2_box_password.addItems(['admin:admin', 'Administrator:9102SerCloudPBX', 'user:1234'])
        self.f_box_change_password(1)
        self.f_box_change_password(2)
        # 绑定选框回调函数
        self.D1_box_password.currentIndexChanged.connect(lambda: self.f_box_change_password(1))
        # 绑定按键回调函数
        self.D1_btn_band.clicked.connect(lambda: self.f_btn_band(1))
        self.D1_btn_autotest.clicked.connect(lambda: self.f_btn_autotest(self.D1))
        self.D1_btn_telnet.clicked.connect(lambda: self.f_btn_telnet(self.D1))
        self.D1_btn_reboot.clicked.connect(lambda: self.f_btn_reboot(self.D1))
        self.D1_btn_factory.clicked.connect(lambda: self.f_btn_factory(self.D1))
        self.D1_btn_ap.clicked.connect(lambda: self.f_btn_ap(self.D1, self.D1_text_fw.text(), self.D1_text_cfg.text()))
        self.D1_btn_pselect.clicked.connect(lambda: self.f_btn_pslect(self.D1, self.D1_text_pnum, self.D1_text_pvalue))
        self.D1_btn_pset.clicked.connect(lambda: self.f_btn_pset(self.D1, self.D1_text_pnum, self.D1_text_pvalue))

    def f_box_change_password(self, tag):
        if (tag == 1):
            self.D1_name = self.D1_box_password.currentText().split(':')[0]
            self.D1_password = self.D1_box_password.currentText().split(':')[1]

        elif tag == 2:
            self.D2_name = self.D2_box_password.currentText().split(':')[0]
            self.D2_password = self.D2_box_password.currentText().split(':')[1]
        else:
            QMessageBox.about(self, '登录提示', 'err')

    @Slot()
    def f_btn_band(self, tag):
        # 检查ip合法性
        if (tag == 1) & isIPv4(self.D1_text_ip.text()):
            self.D1_ip = self.D1_text_ip.text()
            # 检查设备是否在线
            if isOnline(self.D1_ip, self.D1_name, self.D1_password) == 1:
                # 生成设备对象包含ip mac version user password model
                self.D1 = VoipDevice(self.D1_ip, self.D1_name, self.D1_password)
                # 设置页签为model（型号）
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                          QCoreApplication.translate("MainWindow", self.D1.model, None))
                self.set_all_btn(1, True)  # 解锁页面btn
                self.D1_text_fw.setText(query_pnum(self.D1, '192'))
                self.D1_text_cfg.setText(query_pnum(self.D1, '237'))
                self.D1_lab_online.setText('<font color=green>█在线█</font>')

                QMessageBox.about(self, '登录提示', self.D1.user + '绑定成功' + self.D1.model)
            # 设备在线但密码错误
            elif isOnline(self.D1_ip, self.D1_name, self.D1_password) == 0:
                self.D1_lab_online.setText('<font color=red>█失败█</font>')
                self.set_all_btn(1, False)
                QMessageBox.about(self, '登录提示', '密码错误')
            # 设备离线
            else:
                self.D1_lab_online.setText('<font color=red>█离线█</font>')
                self.set_all_btn(1, False)
                QMessageBox.about(self, '登录提示', '无响应')

        elif (tag == 2) & isIPv4(self.D2_text_ip.text()):
            self.D2_ip = self.D2_text_ip.text()
            self.set_all_btn(2, True)
            QMessageBox.about(self, '登录提示', '绑定成功')
        else:
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                      QCoreApplication.translate("MainWindow", "啊1", None))
            QMessageBox.about(self, '登录提示', '绑定失败')

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

    def f_btn_ap(self, device, str_fw_path, str_cfg_path):

        skip_rom_check(device)
        set_pnum(device, 'P192', str_fw_path)
        set_pnum(device, 'P237', str_cfg_path)
        AutoProvisionNow(device)

    def f_btn_pslect(self, device, pnum, pvalue):
        if pnum.text() == '':
            pvalue.setText('')
        else:
            pvalue.setText(query_pnum(device, str(pnum.text())))

    def f_btn_pset(self, device, pnum, pvalue):
        if pnum.text() == '':
            QMessageBox.about(self, '提示', 'P值不能为空')

        else:
            ret = set_pnum(device, 'P'+pnum.text(), pvalue.text())
            self.groupBox_9.setTitle('111')
            if not ret:
                QMessageBox.about(self, '提示', 'P值设置失败')

    def set_all_btn(self, tag, value):
        if (tag in [1, 2, 3]) & (value in [True, False]):
            if tag == 1:
                self.D1_btn_autotest.setEnabled(value)
                self.D1_btn_telnet.setEnabled(value)
                self.D1_btn_reboot.setEnabled(value)
                self.D1_btn_factory.setEnabled(value)
                self.D1_btn_ap.setEnabled(value)
                self.D1_btn_pselect.setEnabled(value)
                self.D1_btn_pset.setEnabled(value)
            elif tag == 2:
                self.D2_btn_autotest.setEnabled(value)
                self.D2_btn_telnet.setEnabled(value)
                self.D2_btn_reboot.setEnabled(value)
                self.D2_btn_factory.setEnabled(value)
                self.D2_btn_ap.setEnabled(value)
                self.D2_btn_pselect.setEnabled(value)
                self.D2_btn_pset.setEnabled(value)

        else:
            return False


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    # w = QMainWindow()
    # gui.ui.setupUi(w)
    # w.show()
    gui.show()
    sys.exit(app.exec_())

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
