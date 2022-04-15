from yaml import safe_load


class HlConfig:
    def __init__(self):
        try:
            self.cfg = safe_load(open('../register_date.yml', 'r', encoding='utf-8').read())
        except Exception:
            print('file not exits')
    def add_option(self,option_name,value):
        pass
    def get_option(self,option_name,value):
        pass
    def save_cfg_file(self):
        pass