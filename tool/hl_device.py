import re
from tool.test_util import hl_request


class VoipDevice:
    def __init__(self, in_ip, in_user, in_password):

        self.ip = in_ip
        self.user = in_user
        self.password = in_password
        text = hl_request('GET', 'http://%s/index.htm' % in_ip, auth=(in_user, in_password), timeout=1).text
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
