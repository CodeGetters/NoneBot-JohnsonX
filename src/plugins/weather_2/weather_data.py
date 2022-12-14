# -*- coding = utf-8 -*-
# @Time: 2022/12/13 22:39
# @Author: JohonsonX
# @File: weather_data.py
# @SoftWare: PyCharm

import requests
import json


def get_data(city_name):
    location = city_name
    API = "https://api.seniverse.com/v3/weather/now.json?key=S5GRMbU8_bsY3_29f&location=LOCAL&language=zh-Hans&unit=c"
    API = API.replace("LOCAL", location)
    result = requests.get(API, timeout=1)
    # str 类型
    data = json.dumps(result.json())
    # 转换成 dict 类型
    data_json = json.loads(data)['results'][0]['now']
    weather = data_json['text']
    temperature = data_json['temperature']
    return [weather, temperature]

# # 测试
# get_data('beijing')
# print(get_data('beijing'))
