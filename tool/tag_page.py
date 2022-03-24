from threading import Thread

from tool.test_tool import query_pnum, set_all_btn, skip_rom_check, set_pnum, AutoProvisionNow
from tool.test_util import check_device_alive, hl_request, loop_check_is_online
from ui.MainWindow import MainWindow


class Tag:
    def __init__(self, ui: MainWindow, tag_number):
        from yaml import safe_load
        self.register_lock_flag = 0
        if tag_number == 1:
            # 页面分类
            self.tab = ui.tab
            # 话机信息
            self.text_ip = ui.D1_text_ip
            self.box_password = ui.D1_box_password
            self.box_password.addItems(['admin:admin', 'Administrator:9102SerCloudPBX', 'user:1234'])  # 添加密码选项内容
            self.btn_band = ui.D1_btn_band
            self.lab_online = ui.D1_lab_online
            self.btn_web = ui.D1_btn_web
            # 功能区
            self.btn_autotest = ui.D1_btn_autotest
            self.btn_telnet = ui.D1_btn_telnet
            self.btn_reboot = ui.D1_btn_reboot
            self.btn_factory = ui.D1_btn_factory
            self.btn_logserver = ui.D1_btn_logserver
            self.logserver_port = 5191
            # 指派区
            self.text_fw = ui.D1_text_fw
            self.text_cfg = ui.D1_text_cfg
            self.btn_ap = ui.D1_btn_ap
            # P值区
            self.text_pnum = ui.D1_text_pnum
            self.text_pvalue = ui.D1_text_pvalue
            self.btn_pselect = ui.D1_btn_pselect
            self.btn_ptxt = ui.D1_btn_ptxt
            self.btn_pset = ui.D1_btn_pset
            # 注册区
            self.box_register = ui.D1_box_register
            self.btn_register = ui.D1_btn_register
            # 保存区
            self.btn_savescreen = ui.D1_btn_savescreen
            self.btn_savelog = ui.D1_btn_savelog
            self.btn_savecfg = ui.D1_btn_savecfg
        elif tag_number == 2:
            # 页面分类
            self.tab = ui.tab_2
            # 话机信息
            self.text_ip = ui.D2_text_ip
            self.box_password = ui.D2_box_password
            self.box_password.addItems(['admin:admin', 'Administrator:9102SerCloudPBX', 'user:1234'])  # 添加密码选项内容
            self.btn_band = ui.D2_btn_band
            self.lab_online = ui.D2_lab_online
            self.btn_web = ui.D2_btn_web
            # 功能区
            self.btn_autotest = ui.D2_btn_autotest
            self.btn_telnet = ui.D2_btn_telnet
            self.btn_reboot = ui.D2_btn_reboot
            self.btn_factory = ui.D2_btn_factory
            self.btn_logserver = ui.D2_btn_logserver
            self.logserver_port = 5192
            # 指派区
            self.text_fw = ui.D2_text_fw
            self.text_cfg = ui.D2_text_cfg
            self.btn_ap = ui.D2_btn_ap
            # P值区
            self.text_pnum = ui.D2_text_pnum
            self.text_pvalue = ui.D2_text_pvalue
            self.btn_pselect = ui.D2_btn_pselect
            self.btn_ptxt = ui.D2_btn_ptxt
            self.btn_pset = ui.D2_btn_pset
            # 注册区
            self.box_register = ui.D2_box_register
            self.btn_register = ui.D2_btn_register
            # 保存区
            self.btn_savescreen = ui.D2_btn_savescreen
            self.btn_savelog = ui.D2_btn_savelog
            self.btn_savecfg = ui.D2_btn_savecfg
        elif tag_number == 3:
            # 页面分类
            self.tab = ui.tab_5
            # 话机信息
            self.text_ip = ui.D3_text_ip
            self.box_password = ui.D3_box_password
            self.box_password.addItems(['admin:admin', 'Administrator:9102SerCloudPBX', 'user:1234'])  # 添加密码选项内容
            self.btn_band = ui.D3_btn_band
            self.lab_online = ui.D3_lab_online
            self.btn_web = ui.D3_btn_web
            # 功能区
            self.btn_autotest = ui.D3_btn_autotest
            self.btn_telnet = ui.D3_btn_telnet
            self.btn_reboot = ui.D3_btn_reboot
            self.btn_factory = ui.D3_btn_factory
            self.btn_logserver = ui.D3_btn_logserver
            self.logserver_port = 5193
            # 指派区
            self.text_fw = ui.D3_text_fw
            self.text_cfg = ui.D3_text_cfg
            self.btn_ap = ui.D3_btn_ap
            # P值区
            self.text_pnum = ui.D3_text_pnum
            self.text_pvalue = ui.D3_text_pvalue
            self.btn_ptxt = ui.D3_btn_ptxt
            self.btn_pselect = ui.D3_btn_pselect
            self.btn_pset = ui.D3_btn_pset
            # 注册区
            self.box_register = ui.D3_box_register
            self.btn_register = ui.D3_btn_register
            # 保存区
            self.btn_savescreen = ui.D3_btn_savescreen
            self.btn_savelog = ui.D3_btn_savelog
            self.btn_savecfg = ui.D3_btn_savecfg
        elif tag_number == 4:
            # 页面分类
            self.tab = ui.tab_6
            # 话机信息
            self.text_ip = ui.D4_text_ip
            self.box_password = ui.D4_box_password
            self.box_password.addItems(['admin:admin', 'Administrator:9102SerCloudPBX', 'user:1234'])  # 添加密码选项内容
            self.btn_band = ui.D4_btn_band
            self.lab_online = ui.D4_lab_online
            self.btn_web = ui.D4_btn_web
            # 功能区
            self.btn_autotest = ui.D4_btn_autotest
            self.btn_telnet = ui.D4_btn_telnet
            self.btn_reboot = ui.D4_btn_reboot
            self.btn_factory = ui.D4_btn_factory
            self.btn_logserver = ui.D4_btn_logserver
            self.logserver_port = 5194
            # 指派区
            self.text_fw = ui.D4_text_fw
            self.text_cfg = ui.D4_text_cfg
            self.btn_ap = ui.D4_btn_ap
            # P值区
            self.text_pnum = ui.D4_text_pnum
            self.text_pvalue = ui.D4_text_pvalue
            self.btn_pselect = ui.D4_btn_pselect
            self.btn_ptxt = ui.D4_btn_ptxt
            self.btn_pset = ui.D4_btn_pset
            # 注册区
            self.box_register = ui.D4_box_register
            self.btn_register = ui.D4_btn_register
            # 保存区
            self.btn_savescreen = ui.D4_btn_savescreen
            self.btn_savelog = ui.D4_btn_savelog
            self.btn_savecfg = ui.D4_btn_savecfg
        try:
            self.box_register.addItems(
                list(safe_load(open('register_date.yml', 'r', encoding='utf-8').read())))  # 添加注册选框内容
            self.register_lock_falg = 0
        except Exception:
            self.box_register.addItems(['请检查register_date.yml'])
            self.register_lock_flag = 1

    def connect_state(self, state):
        if state in [True, False]:
            set_all_btn(self, state)
            if state is False:
                self.lab_online.setText('<font color=red>█离线█</font>')
            else:
                self.lab_online.setText('<font color=green>█在线█</font>')
        else:
            print('connect state fail')

    def refresh_state(self):
        try:
            self.text_fw.setText(query_pnum(self.device, '192'))
            self.text_cfg.setText(query_pnum(self.device, '237'))
            if self.text_pnum.text() == '':
                self.text_pvalue.setText('')
            else:
                self.text_pvalue.setText(query_pnum(self.device, str(self.text_pnum.text())))
            return True
        except Exception:
            return False

    def clean_state(self):
        self.text_fw.setText('')
        self.text_cfg.setText('')
        self.text_pvalue.setText('')

    def exec_autotest(self, window):
        """执行 enable_autotest_api"""
        device = self.device
        if check_device_alive(window, self) is False:
            window.show_message('auto test 失败: check_device_alive 失败', 1)
            return False
        window.show_message('执行 auto test 中')
        url = 'http://%s/enable_autotest_api' % device.ip
        r = hl_request('GET', url, auth=(device.user, device.password), timeout=1)
        if r.status_code != 200:
            window.show_message('auto test 失败:%s' % r.status_code, 1)
            return False
        window.show_message('auto test 成功')
        return True

    def exec_telnet(self, window):
        device = self.device
        """执行 enable telnet 和 enable ftp"""
        window.show_message('执行 telnet 中')
        if self.exec_autotest(window) is False:
            window.show_message('telnet 失败:auto test 失败', 1)
            return False
        url1 = 'http://%s/AutoTest&action=enabletelnet' % device.ip
        r = hl_request('GET', url1, auth=(device.user, device.password), timeout=1)
        if r.status_code != 200:
            window.show_message('telnet 失败:%s' % r.status_code, 1)
            return False
        url2 = 'http://%s/AutoTest&action=enableftp' % device.ip
        r = hl_request('GET', url2, auth=(device.user, device.password), timeout=1)
        if r.status_code != 200:
            window.show_message('ftp 失败:%s' % r.status_code, 1)
            return False
        window.show_message('telnet 成功')
        return True

    def exec_reboot(self, window):
        """重启话机"""
        device = self.device
        url = 'http://%s/rb_phone.htm' % device.ip
        r = hl_request('GET', url, auth=(device.user, device.password), timeout=1)
        if r.status_code != 200:
            window.show_message('话机重启失败：%s' % r.status_code, 1)
            return False
        window.show_message('话机正在重启')
        self.connect_state(False)
        self.lab_online.setText('<font color=red>█重启█</font>')
        temp = loop_check_is_online(self)
        if temp is True:
            window.show_message('话机启动成功')
            return True
        else:
            window.show_message('话机仍未成功', 1)
            return False

    def exec_factory(self, window):
        """恢复出厂"""
        device = self.device
        if self.exec_autotest(window) is False:
            window.show_message('话机恢复出厂失败:autotest 失败', 1)
            window.show_message('reset factory失败: autotest 失败', 1)
            return False
        url = 'http://%s/Abyss/FactoryReset' % device.ip
        r = hl_request('GET', url, auth=(device.user, device.password), timeout=1)
        if r.status_code != 200:
            window.show_message('话机恢复出厂失败:%s' % r.status_code, 1)
            return False
        window.show_message('话机正在重启')
        self.connect_state(False)
        self.lab_online.setText('<font color=red>█重启█</font>')
        temp = loop_check_is_online(self)
        if temp is True:
            window.show_message('话机启动成功')
            return True
        else:
            window.show_message('话机仍未成功', 1)
            return False

    def exec_ap(self, window):
        """设置fw和cfg地址并执行skip rom check"""
        if skip_rom_check(self.device) is False:
            window.show_message('ap失败：skip_rom_check失败', 1)
            return False
        set_pnum(self.device, 'P192', self.text_fw.text())
        set_pnum(self.device, 'P237', self.text_cfg.text())
        if AutoProvisionNow(self.device) is False:
            window.show_message('ap失败：AutoProvisionNow失败', 1)
            return False
        window.show_message('ap成功！')
        return True

    def exec_select_p(self,window):
        if self.refresh_state() is False:
            window.show_message('P值查询失败',1)
            return False
        window.show_message('P值查询成功')
        return True

