import yaml
from yaml import safe_load


class HlConfig:
    def __init__(self):
        try:
            self.cfg = safe_load(open('./config.yml', 'r', encoding='utf-8').read())
        except FileNotFoundError:
            pass

    def add_option(self, option_name, value):
        print(self.cfg.keys())
        if option_name in self.cfg.keys():
            print(self.cfg[option_name])
            if value in self.cfg[option_name]:
                print('参数已存在')
                return False
            else:
                self.cfg[option_name].append(value)
                self.save_cfg_file()
                return True
        else:
            print('配置项不存在')
            return False

    def set_option(self, option_name, value):
        if option_name in self.cfg.keys():
            print(self.cfg[option_name])
            self.cfg[option_name] = [value]
            self.save_cfg_file()
            return True
        else:
            print('配置项不存在')
            return False

    def get_option(self, option_name):
        return self.cfg[option_name]

    def save_cfg_file(self):
        yaml.safe_dump(self.cfg, open('./config.yml', 'w'))


hlcfg = HlConfig()