import requests


def request(method, url, **kwargs):
    print('send %s request to %s' % (method, url))
    req = requests.request(method, url, **kwargs)
    if req.status_code == 401:
        req = requests.request(method, url, **kwargs)
    return req


def isIPv4(ip_str):
    ip_list = ip_str.split('.')
    if ip_str.count('.') != 3:  # 判断是否有三个点，正确的IPV4地址为 X.X.X.X
        return False
    else:
        flag = True
        # for循环遍历list中的所有元素
        for num in ip_list:
            # try except 强转字符串错误那么元素不是int类型
            try:
                # 强转类型为int，符合比较的预期
                ip_num = int(num)
                # 判断第一位不是0，且属于0-255区间
                if ip_list[0] != '0':
                    if (ip_num >= 0) & (ip_num <= 255):
                        pass
                    else:
                        flag = False
                else:
                    flag = False
                    break
            except Exception:
                flag = False
            if num == str(ip_num):
                pass
            else:
                flag = False
                break
        return flag


def isOnline(ip, user, password):
    try:
        r = request('GET', 'http://%s/index.htm' % ip, auth=(user, password), timeout=1)
        if r.status_code == 200:
            return 1
        else:
            return 0
    except Exception:
        return 2
