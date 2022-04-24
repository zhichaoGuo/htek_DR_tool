import re
from tool.test_util import hl_request

rom_1= [['fw500M.rom','UC501'],
        ['fw520M.rom','UC503G','UC505','UC507','CIP250V1','CIP270V1'],
        ['fw520U.rom','UC505U','UC507U','CIP250V2','CIP270V2'],
        ['fw900M.rom','UC912G','UC902'],
        ['fw910M.rom','UC921G','UC902S'],
        ['fw920M.rom','UC923','UC924','UC924E','UC926','UC926E'],
        ['fw920U.rom','UC923U','UC924U','UC924W','UC926U','UC926S'],
        ['fw930M.rom','UC921E']]


class VoipDevice:
    def __init__(self, in_ip, in_user, in_password):
        self.ip = in_ip
        self.user = in_user
        self.password = in_password
        text = hl_request('GET', 'http://%s/index.htm' % in_ip, auth=(in_user, in_password)).text
        self.mac = self._getMac(text)
        self.model = self._getModel(text)
        self.version = self._getVersion(text)

    def _getMac(self,text):
        re_1 = 'jscs.mac_address'
        re_2 = '</td>'
        text = text[re.search(re_1, text, re.U).span()[1] + 45:]
        text = text[:re.search(re_2, text, re.U).span()[0]]
        return text

    def _getModel(self,text):
        re_1 = 'jscs.product_type'
        re_2 = '</td>'
        text = text[re.search(re_1, text, re.U).span()[1] + 44:]
        text = text[:re.search(re_2, text, re.U).span()[0]]
        return text

    def _getVersion(self,text):
        re_1 = 'ROM--'
        re_2 = '\('
        text = text[re.search(re_1, text, re.U).span()[1]:]
        text = text[:re.search(re_2, text, re.U).span()[0]]
        return text

    def _getRom(self):
        text = ''
        for i in range(len(rom_1)):
            if self.model in rom_1[i]:
                text = rom_1[i][0]
                break
        return text