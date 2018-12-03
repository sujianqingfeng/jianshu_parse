import re

import requests
from bs4 import BeautifulSoup

import tomd


def main():
    headers = {
        'referer': 'https://www.jianshu.com/p/c75f1ce0a6ae',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }

    url = 'https://www.jianshu.com/p/c75f1ce0a6ae'

    res = requests.get(url=url, headers=headers)

    # print(res.text)

    soup = BeautifulSoup(res.text)

    content = soup.select_one('div.show-content-free')
    # print(content)

    m = re.search('div\sclass="show-content-free">([\s\S]*)</div>', str(content))
    if m:
        html = m.group(1)
        print(html)
        tomd.Tomd(html=html, file='test.md').export()


if __name__ == '__main__':
    main()
