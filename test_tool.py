from urllib import parse

from test_util import request


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
    except Exception as err:
        print("postFormToDevice err:", err)
        return False
    return True
