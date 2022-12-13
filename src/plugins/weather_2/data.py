# -*- coding = utf-8 -*-
# @Time: 2022/12/13 22:39
# @Author: JohonsonX
# @File: data.py
# @SoftWare: PyCharm

import requests

# from __init__ import city_name


location = "天津"
API = "https://api.seniverse.com/v3/weather/now.json?key=S5GRMbU8_bsY3_29f&location=LOCAL&language=zh-Hans&unit=c"
API = API.replace("LOCAL", location)


def get_data():
    result = requests.get(API, timeout=1)
    return result


print(get_data())
