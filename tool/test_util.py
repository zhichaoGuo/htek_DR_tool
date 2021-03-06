from datetime import datetime
from os.path import abspath
from threading import Thread
from time import sleep

import requests
import xml.etree.ElementTree as ET

from PySide2.QtWidgets import QFileDialog


def hl_request(method, url, **kwargs):
    try:
        print('send %s request to %s' % (method, url))
        req = requests.request(method, url, **kwargs)
        if req.status_code == 401:
            req = requests.request(method, url, **kwargs)
        return req
    except:
        class fail:
            status_code = 'request 错误'
        req = fail()
        return req


def isIPv4(ip_str):
    ip_list = ip_str.split('.')
    if ip_str.count('.') != 3:  # 判断是否有三个点，正确的IPV4地址为 X.X.X.X
        return False
    else:
        flag = True
        # for循环遍历list中的所有元素
        for num in ip_list:
            # try except 强转字符串错误那么元素不是int类型
            try:
                # 强转类型为int，符合比较的预期
                ip_num = int(num)
                # 判断第一位不是0，且属于0-255区间
                if ip_list[0] != '0':
                    if (ip_num >= 0) & (ip_num <= 255):
                        pass
                    else:
                        flag = False
                else:
                    flag = False
                    break
            except Exception:
                flag = False
            if num == str(ip_num):
                pass
            else:
                flag = False
                break
        return flag


def isOnline(ip, user, password):
    try:
        r = hl_request('GET', 'http://%s/index.htm' % ip, auth=(user, password), timeout=1)
        if r.status_code == 200:
            return 1
        else:
            return 0
    except Exception:
        return 2


def parsePhoneStatusXml(xml):
    retXmlInfo = dict()
    root = ET.fromstring(xml)
    for testInfo in root.findall('info'):
        name = testInfo.get('name')
        if not name:
            raise Exception("no name in testInfo")
        value = testInfo.get('value')
        if not value:
            value = ''
            # raise Exception("no value in testInfo")
        retXmlInfo[name] = value
    return retXmlInfo


def return_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    print('server ip is %s' % ip)
    s.close()
    return ip


def save_file(window, file_buf, model, file_methd):
    try:
        file_name = '[' + str(datetime.now())[5:].replace(":", "·").replace("-", "").split(".")[0].replace(" ", "]")
        file_name = file_name.split(']')[0] + f'][{model}]' + file_name.split(']')[1]
        filePath = QFileDialog.getSaveFileName(window, '保存路径', f'{abspath(".")}\\screen\\{file_name}.{file_methd}',
                                               f'.{file_methd}(*.{file_methd})')
        try:
            with open(filePath[0], "wb") as f:
                f.write(file_buf)
            f.close()
            window.show_message('保存%s文件成功' % file_methd)
            from os import system
            thread = Thread(target=system, args=[f"{filePath[0]}", ])
            thread.setDaemon(True)
            thread.start()
            return filePath[0]
        except FileNotFoundError:
            window.show_message('取消保存%s文件' % file_methd)
    except TypeError:
        window.show_message('save_file:TypeError',1)
        return False

def loop_check_is_online(tag, timeout=50, sleep_time=36):
    device = tag.device
    sleep(sleep_time)
    for i in range(timeout):
        sleep(4)
        if isOnline(device.ip, device.user, device.password) == 1:
            tag.refresh_state()
            tag.connect_state(True)
            return True
    print('still not online')
    tag.clean_state()
    tag.connect_state(False)
    tag.lab_online.setText('<font color=red>█离线█</font>')
    return False


def check_device_alive(window, tag):
    device = tag.device
    state_code = isOnline(device.ip, device.user, device.password)
    if state_code == 1:
        tag.connect_state(True)
        return True
    elif state_code == 0:
        tag.clean_state()
        tag.connect_state(False)
        window.show_message('话机密码有误', 1)
    elif state_code == 2:
        tag.clean_state()
        tag.connect_state(False)
        window.show_message('话机未响应', 1)

def get_abyss_device_info(window):
    pass