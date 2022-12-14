# -*- coding = utf-8 -*-
# @Time: 2022/12/13 21:28
# @Author: JohonsonX
# @File: __init__.py
# @SoftWare: PyCharm

# 引入事件响应器模块
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.adapters.onebot.v11 import Bot, Message
from .weather_data import get_data
import emoji

'''
最近几天的天气
命令：天气
该API只能查询省会以下的城市
支持直辖市
'''

weather = on_command("weather", rule=to_me(), aliases={'实况天气', '天气02'}, priority=5)


# 消息处理
@weather.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    # 提取消息内的纯文本
    megText = args.extract_plain_text()
    if megText:
        # 设置一个got消息，获取 city
        matcher.set_arg("city", args)


# 获取城市参数
welcome = emoji.emojize(
    '欢迎来到天气查询功能:sparkles:\n请问您需要查询的天气是...\n目前支持查询的城市有\n北京、天津、石家庄、德阳、遵义')


@weather.got("city", prompt=welcome)
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    # 如果参数不符合，重新输入
    if city_name not in ["北京", '德阳', '天津', '遵义', '重庆', '石家庄']:
        # 错误消息处理
        await weather.reject(city.template('你要查询的城市 {city} 暂时不支持查询，请重新输入支持查询的城市'))
    # 获得天气信息
    infor = get_data(city_name)
    results = "今日该城市的天气为：" + infor[0] + "\r\n温度：" + infor[1]
    await weather.finish(results)
