import yaml
from yaml import safe_load


class HlConfig:
    def __init__(self):
        try:
            self.cfg = safe_load(open('./config.yml', 'r', encoding='utf-8').read())
            self.load_state = True
        except FileNotFoundError:
            self.load_state = False

    def add_option(self, option_name, value):
        if self.load_state is True:
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
        else:
            return False

    def set_option(self, option_name, value):
        if self.load_state is True:
            if option_name in self.cfg.keys():
                print(self.cfg[option_name])
                self.cfg[option_name] = [value]
                self.save_cfg_file()
                return True
            else:
                print('配置项不存在')
                return False
        else:
            return False

    def get_option(self, option_name):
        if self.load_state is True:
            return self.cfg[option_name]
        else:
            return False

    def save_cfg_file(self):
        if self.load_state is True:
            yaml.safe_dump(self.cfg, open('./config.yml', 'w'))
            return True
        else:
            print('config.yml load err')
            return False


hlcfg = HlConfig()
