import threading
from datetime import datetime
from os.path import abspath
from urllib import parse

from PySide2.QtWidgets import QFileDialog

from tool.test_util import hl_request, parsePhoneStatusXml


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

        req = hl_request('POST', url, headers=headers, data=data, auth=auth)
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

        req = hl_request('POST', url, headers=headers, data=data, auth=auth)
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
        req = hl_request('GET', url, auth=auth)
        if req.status_code == 200:
            return parsePhoneStatusXml(req.text)[pnum]
        else:
            return '未能获取P%s' % pnum
    except Exception as err:
        print("query_pnum err:", err)
        return '未能发送请求获取%s' % pnum


def skip_rom_check(device):
    url = "http://%s/skip_rom_check" % device.ip
    auth = (device.user, device.password)
    try:
        req = hl_request('GET', url, auth=auth)
        if req.status_code == 200:
            return True
    except Exception as err:
        print("skip_rom_check err:", err)
        return False
    return True


def AutoProvisionNow(device):
    pValues = {"P900000": ''}
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    url = "http://%s/now_auto_provision.htm" % device.ip
    auth = (device.user, device.password)
    try:
        data = parse.urlencode(pValues).encode(encoding="utf-8")
        req = hl_request('POST', url, headers=headers, data=data, auth=auth)
        if req.status_code == 200:
            return True
    except Exception as err:
        print("AutoProvisionNow err:", err)
        return False
    return True


def save_screen(device):
    url = "http://%s/download_screen" % device.ip
    auth = (device.user, device.password)
    try:
        r = hl_request('GET', url, auth=auth)
        return r.content
    except Exception as err:
        print('can not send request to save_screen :%s' % err)
        return False

def save_syslog(windows,device):
    url = "http://%s/download_syslog" % device.ip
    auth = (device.user, device.password)
    r = hl_request('GET',url,auth=auth)
    syslog_data = r.content
    file_name = '[' + str(datetime.now())[5:].replace(":", "·").replace("-", "").split(".")[0].replace(" ", "]")
    file_name = file_name.split(']')[0] + f'][{device.model}]' + file_name.split(']')[1]
    filePath = QFileDialog.getSaveFileName(windows, '保存路径', f'{abspath(".")}\\screen\\{file_name}.txt', '.txt(*.txt)')
    with open(filePath[0], "wb") as f:
        f.write(syslog_data)
    f.close()

if __name__ == '__main__':
    pass
