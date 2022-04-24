import json

import requests


class AbyssInfo:
    def __init__(self):
        self.device = []
        from tool.config import hlcfg
        url = hlcfg.get_option('abyss_server')[0]+ 'phonedatas'
        try:
            r = requests.get(url)
            for i in json.loads(r.text)['data']:
                if i['online'] is True:
                    self.device.append(i)
        except Exception:
            print('服务器不可达')

    def less_info(self):
        less = []
        for dev in self.device:
            less.append([dev['model'], dev['ip'], dev['mac'], dev['version'], dev['app'], dev['state']])
        return less

