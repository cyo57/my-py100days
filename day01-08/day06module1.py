'''一个测试用例'''
import requests


def get_html(url, time=5):
    '''传入url返回文本, 5s超时'''
    res = requests.get(url, timeout=time)
    res.raise_for_status()
    res.encoding = res.apparent_encoding
    return res.text

# 此写法import时不会被运行
if __name__ == '__main__':
    print(get_html('http://sky.yunshangbandao.top'))
