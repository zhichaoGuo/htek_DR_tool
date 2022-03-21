from yaml import safe_load

from tool.test_tool import query_pnum
from ui.MainWindow import MainWindow


class Tag:
    def __init__(self, ui: MainWindow, tag_number):
        if tag_number == 1:
            # 页面分类
            self.tab = ui.tab
            # 话机信息
            self.text_ip = ui.D1_text_ip
            self.box_password = ui.D1_box_password
            self.box_password.addItems(['admin:admin', 'Administrator:9102SerCloudPBX', 'user:1234'])  # 添加密码选项内容
            self.btn_band = ui.D1_btn_band
            self.lab_online = ui.D1_lab_online
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
            self.box_register.addItems(
                list(safe_load(open('register_date.yml', 'r', encoding='utf-8').read())))  # 添加注册选框内容
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
            self.box_register.addItems(
                list(safe_load(open('register_date.yml', 'r', encoding='utf-8').read())))  # 添加注册选框内容
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
            self.box_register.addItems(
                list(safe_load(open('register_date.yml', 'r', encoding='utf-8').read())))  # 添加注册选框内容
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
            self.box_register.addItems(
                list(safe_load(open('register_date.yml', 'r', encoding='utf-8').read())))  # 添加注册选框内容
            self.btn_register = ui.D4_btn_register
            # 保存区
            self.btn_savescreen = ui.D4_btn_savescreen
            self.btn_savelog = ui.D4_btn_savelog
            self.btn_savecfg = ui.D4_btn_savecfg

    def connect_state(self,state):
        if state in [True,False]:
            MainWindow.set_all_btn(self,state)
            if state is False:
                self.lab_online.setText('<font color=red>█离线█</font>')
            else:
                self.lab_online.setText('<font color=green>█在线█</font>')
        else:
            print('connect state fail')

    def refresh_state(self):
        self.text_fw.setText(query_pnum(self.device, '192'))
        self.text_cfg.setText(query_pnum(self.device, '237'))
        if self.text_pnum.text() == '':
            self.text_pvalue.setText('')
        else:
            self.text_pvalue.setText(query_pnum(self.device, str(self.text_pnum.text())))

    def clean_state(self):
        self.text_fw.setText('')
        self.text_cfg.setText('')
        self.text_pvalue.setText('')