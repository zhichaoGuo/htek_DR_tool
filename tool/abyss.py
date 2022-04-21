import json

import requests


class AbyssInfo:
    device = []

    def __init__(self):
        url = 'http://abyss.htek.com:5001/phonedatas'
        r = requests.get(url)
        for i in json.loads(r.text)['data']:
            if i['online'] is True:
                self.device.append(i)


def less_info_device(device:list):
    less = []
    for dev in device:
        less.append([dev['model'],dev['ip'],dev['mac'],dev['version'],dev['app'],dev['state']])
    return less
