import time
from webbrowser import open as open_page
from urllib import parse

from tool.test_util import hl_request, parsePhoneStatusXml, loop_check_is_online


def web_add_contacts(device, xmlfile_abs_path):
    url = 'http://%s/hl_web/contact_post' % device.ip
    try:
        header = {
            "Content-Type": "application/octet-stream"
        }
        data = bytes('phonebook_update:', encoding='utf-8') + b'\xef\xbb\xbf' + open(xmlfile_abs_path, 'rb').read()
        req = hl_request('POST', url, auth=(device.user, device.password), data=data, headers=header)
        if req.status_code == 200:
            return True
        else:
            return False
    except Exception as err:
        print('err:' + str(err))
        return False


def set_pnum(device, pnum: str, value):
    url = "http://%s/save_managerment.htm" % device.ip
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    auth = (device.user, device.password)
    try:
        data = parse.urlencode({pnum: value}).encode(encoding="utf-8")

        req = hl_request('POST', url, headers=headers, data=data, auth=auth, timeout=1)
        if req.status_code == 200:
            return True
        else:
            return False
    except Exception as err:
        print("postFormToDevice err:", err)
        return False


def set_pnums(device, dic):
    url = "http://%s/save_managerment.htm" % device.ip
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    auth = (device.user, device.password)
    try:
        data = parse.urlencode(dic).encode(encoding="utf-8")

        req = hl_request('POST', url, headers=headers, data=data, auth=auth, timeout=1)
        if req.status_code == 200:
            return True
        else:
            return False
    except Exception as err:
        print("postFormToDevice err:", err)
        return False


def query_pnum(device, pnum: str):
    pnum = 'P' + pnum
    url = "http://%s/Abyss/GetPhoneStatus?P=%s" % (device.ip, pnum)
    auth = (device.user, device.password)
    try:
        req = hl_request('GET', url, auth=auth, timeout=1)
        if req.status_code == 200:
            return parsePhoneStatusXml(req.text)[pnum]
        else:
            return '未能获取%s' % pnum
    except Exception as err:
        print("query_pnum err:", err)
        return '未能发送请求获取%s' % pnum


def skip_rom_check(device):
    url = "http://%s/skip_rom_check" % device.ip
    auth = (device.user, device.password)
    try:
        req = hl_request('GET', url, auth=auth, timeout=1)
        if req.status_code == 200:
            return True
        else:
            return False
    except Exception as err:
        print("skip_rom_check err:", err)
        return False


def AutoProvisionNow(device):
    pValues = {"P900000": ''}
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    url = "http://%s/now_auto_provision.htm" % device.ip
    auth = (device.user, device.password)
    try:
        data = parse.urlencode(pValues).encode(encoding="utf-8")
        req = hl_request('POST', url, headers=headers, data=data, auth=auth, timeout=1)
        if req.status_code == 200:
            return True
        else:
            return False
    except Exception as err:
        print("AutoProvisionNow err:", err)
        return False


def save_screen(window, device):
    url = "http://%s/download_screen" % device.ip
    auth = (device.user, device.password)
    try:
        r = hl_request('GET', url, auth=auth)
        if r.status_code != 200:
            print('save screen fild :%s' % r.status_code)
            return -1
    except Exception as err:
        print('save screen fild:%s' % err)
        return -1
    window.file = r.content
    window.file_model = device.model
    window.file_methd = 'bmp'
    window.HlSignal.save_file.emit(window, r.content, device.model, 'bmp')


def save_syslog(window, device):
    url = "http://%s/download_log" % device.ip
    auth = (device.user, device.password)
    try:
        r = hl_request('GET', url, auth=auth)
        if r.status_code != 200:
            print('save sysylog fild :%s' % r.status_code)
            return -1
    except Exception as err:
        print('save sysylog fild ')
        return -1
    window.file = r.content
    window.file_model = device.model
    window.file_methd = 'txt'
    window.HlSignal.save_file.emit(window, window.file, window.file_model, window.file_methd)


def save_xml_cfg(window, device):
    url = "http://%s/download_xml_cfg" % device.ip
    auth = (device.user, device.password)
    try:
        r = hl_request('GET', url, auth=auth)
        if r.status_code != 200:
            print('save xml_cfg fild :%s' % r.status_code)
            return -1
    except Exception as err:
        print('save xml_cfg fild ')
        return -1
    window.file = r.content
    window.file_model = device.model
    window.file_methd = 'xml'
    window.HlSignal.save_file.emit(window, window.file, window.file_model, window.file_methd)


def open_web(device):
    url = "http://%s/" % device.ip
    try:
        open_page(url)
        return True
    except Exception as err:
        print(err)
        return False


def set_all_btn(tag, value):
    if value in [True, False]:
        tag.btn_web.setEnabled(value)
        tag.btn_autotest.setEnabled(value)
        tag.btn_telnet.setEnabled(value)
        tag.btn_reboot.setEnabled(value)
        tag.btn_factory.setEnabled(value)
        tag.btn_inport_rom.setEnabled(value)
        tag.btn_inport_cfg.setEnabled(value)
        tag.btn_ap.setEnabled(value)
        tag.btn_pselect.setEnabled(value)
        tag.btn_pset.setEnabled(value)
        tag.btn_logserver.setEnabled(value)
        tag.btn_calllog.setEnabled(value)
        if tag.register_lock_flag == 1:
            tag.btn_register.setEnabled(False)
        else:
            tag.btn_register.setEnabled(value)
        tag.btn_reset_account.setEnabled(value)
        tag.btn_savescreen.setEnabled(value)
        tag.btn_savelog.setEnabled(value)
        tag.btn_savecfg.setEnabled(value)


def WebImportRom(window,tag,rom_abs_path:str):
    rom_abs_path=rom_abs_path.replace('\\','\\\\')
    device = tag.device
    skip_rom_check = 'http://%s/skip_rom_check' % device.ip
    url = 'http://%s/upgrade_upload' % device.ip
    auth = (device.user, device.password)
    files = {'file': open(rom_abs_path, 'rb')}
    r = hl_request('get',skip_rom_check,auth=auth)
    if r.status_code != 200 :
        print('send request to skip rom check fail :%s' % r.status_code)
        window.show_message('导入rom失败：skip rom check fail',1)
        set_all_btn(tag,True)
        return False
    try:
        r = hl_request('POST',url,auth=auth,files=files)
        if r.status_code == 401:
            print('send request to upgrade return code is 401 , try again')
            r = hl_request('POST', url, auth=auth, files=files)
            if r.status_code != 200:
                window.show_message('导入rom失败：两次导入均失败',1)
                set_all_btn(tag,True)
                return False
        window.show_message('导入rom成功！正在升级')
    except Exception as err:
        print('导入rom失败 :%s' % err)
        set_all_btn(tag,True)
        return False
    tag.lab_online.setText('<font color=red>█升级█</font>')
    time.sleep(100)
    temp = loop_check_is_online(tag)
    if temp is True:
        window.show_message('话机启动成功')
        set_all_btn(tag, True)
        return True
    else:
        window.show_message('话机仍未成功', 1)
        return False

def WebImportXmlCfg(window, tag, xml_abs_path: str):
    device = tag.device
    url = 'http://%s/HLCFG_XML_configuration.htm'% device.ip
    auth = (device.user, device.password)
    files = {
        'file': ('cfg.xml', open(xml_abs_path, 'rb').read(), "text/xml")
    }
    try:
        r = hl_request('POST',url,auth=auth,files=files)
        if r.status_code==200:
            window.show_message('话机导入xml成功！')
            tag.lab_online.setText('<font color=red>█重启█</font>')
            time.sleep(10)
            temp = loop_check_is_online(tag)
            if temp is True:
                window.show_message('话机启动成功')
                set_all_btn(tag, True)
                return True
            else:
                window.show_message('话机仍未启动成功', 1)
                return False
        else:
            window.show_message('话机导入xml失败：%s' % r.status_code, 1)
            set_all_btn(tag, True)
    except Exception as err:
        window.show_message('话机导入xml失败：%s' % err,1)
        set_all_btn(tag, True)
        return False

if __name__ == '__main__':
    pass
