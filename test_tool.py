from urllib import parse

from test_util import request, parsePhoneStatusXml


def web_add_contacts(device, xmlfile_abs_path):
    url = 'http://%s/hl_web/contact_post' % device.ip
    try:
        header = {
            "Content-Type": "application/octet-stream"
        }
        data = bytes('phonebook_update:', encoding='utf-8') + b'\xef\xbb\xbf' + open(xmlfile_abs_path, 'rb').read()
        req = request('POST', url, auth=(device.user, device.password), data=data, headers=header)
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

        req = request('POST', url, headers=headers, data=data, auth=auth)
        if req.status_code == 200:
            return True
        else:
            return False
    except Exception as err:
        print("postFormToDevice err:", err)
        return False

def set_pnums(device,dic):
    url = "http://%s/save_managerment.htm" % device.ip
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    auth = (device.user, device.password)
    try:
        data = parse.urlencode(dic).encode(encoding="utf-8")

        req = request('POST', url, headers=headers, data=data, auth=auth)
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
        req = request('GET', url, auth=auth)
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
        req = request('GET', url, auth=auth)
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
        req = request('POST', url, headers=headers, data=data, auth=auth)
        if req.status_code == 200:
            return True
    except Exception as err:
        print("AutoProvisionNow err:", err)
        return False
    return True


if __name__ == '__main__':
    pass
