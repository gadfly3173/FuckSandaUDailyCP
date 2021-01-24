# -*- coding: utf-8 -*-
import requests
import datetime
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

today = datetime.date.today().strftime("%Y-%m-%d")

# TODO 13位时间戳
ts =
# TODO 32位decodes header
decodes = ''
# TODO 你的data dict/json形式填入即可
data = {
}


def main():
    session = requests.session()
    session.mount('http://', HTTPAdapter(max_retries=Retry(total=50, method_whitelist=frozenset(['GET', 'POST']))))
    b_headers = {
        'Host': '202.121.174.56:8089',
        'Proxy-Connection': 'keep-alive',
        'Content-Length': str(len(data)),
        'ts': str(ts),
        'Origin': 'http://202.121.174.56:8089',
        'decodes': decodes,
        'User-Agent': 'Mozilla/5.0 (Linux; Future; Quantem Computer/ver648; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36  cpdaily/8.2.9 wisedu/8.2.9',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'X-Requested-With': 'om.wisedu.cpdaily',
        'Referer': 'http://202.121.174.56:8089/allApps/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    b = session.post('http://202.121.174.56:8089/report/report/todayReport', json=data, headers=b_headers, timeout=5)
    print(b.text)


main()
