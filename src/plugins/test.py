# -*- coding = utf-8 -*-
# @Time: 2022/12/15 22:13
# @Author: JohonsonX
# @File: test.py
# @SoftWare: PyCharm

import requests


def get_talk():
    url = 'https://api.mcloc.cn/love'
    result = requests.get(url=url, timeout=30)
    result_text = result.text
    return result_text


print(get_talk())
