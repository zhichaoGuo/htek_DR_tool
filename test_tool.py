import requests


def web_add_contacts():
    auth = ('admin', 'admin')
    url = 'http://10.20.0.31/hl_web/contact_post'
    xmlfile = 'G:\\HTTP\\phonebook\\phonebook13.xml'
    try:
        header = {
            "Content-Type": "application/octet-stream"
        }
        data = bytes('phonebook_update:', encoding='utf-8') + b'\xef\xbb\xbf' + open(xmlfile, 'rb').read()

        print(data)
        req = requests.post( url, auth=auth, data=data, headers=header)
        if req.status_code == 200:
            return True
    except Exception as err:
        print('err:' + str(err))