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
from data import get_data

'''
最近几天的天气
命令：天气
'''
weather = on_command("weather", rule=to_me(), aliases={'天气'}, priority=5)
city_name = ""


# 消息处理
@weather.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    # 提取消息内的纯文本
    megText = args.extract_plain_text()
    if megText:
        # 设置一个got消息，获取 city
        matcher.set_arg("city", args)


# 获取城市参数
@weather.got("city", prompt="请问您需要查询的天气是...")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    # 如果参数不符合，重新输入
    if city_name not in ["贵州", "北京", "新疆"]:
        # 错误消息处理
        await weather.reject(city.template('你要查询的城市 {{city}} 不存在，请重新输入'))
    city_weather = await get_weather(city_name)
    await weather.finish(city_name)


async def get_weather(city_name: str) -> str:
    data = get_data(city_name).text
    return "今日天气为："+data
