# -*- coding = utf-8 -*-
# @Time: 2022/12/11 19:45
# @Author: JohonsonX
# @File: weather_01.py
# @SoftWare: PyCharm

# 引入事件响应器模块
from nonebot import on_command
# 引入事件响应器匹配规则模块(@bot才会响应事件)
from nonebot.rule import to_me
# 引入创建与运行事件响应器模块
from nonebot.matcher import Matcher
# 引入事件处理流程模块
from nonebot.adapters import Message
# Arg:参数模块
# CommandArg:获取命令型消息命令后跟随的参数
# ArgPlainText:获取某次got接收的参数的纯文本
from nonebot.params import Arg, CommandArg, ArgPlainText

# rule=to_me()：匹配与机器人有关的事件
# 事件函数名 = "事件响应器名", rule=to_me,[aliases = {'响应关键词'}],优先级
weather = on_command("weather", rule=to_me(), aliases={"天气01", "天气预报"}, priority=5)


# 获取用户发送的消息内容
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    # 首次发送命令时跟随的参数，例如：/天气 上海，则 args 为上海
    # 提取消息内纯文本消息
    plain_text = args.extract_plain_text()
    if plain_text:
        # 如果用户发送了参数则直接赋值
        matcher.set_arg("city", args)


# 装饰一个函数来指示机器人获取一个参数
# prompt：参数不存在时向用户发送的消息
@weather.got("city", prompt="请问你要查询的天气是哪一个城市的天气嘞？")
# 获取城市参数
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    # 如果参数不符合要求，则提示用户重新输入
    if city_name not in ["天津", "贵州", "四川", '北京', '河北']:
        # 可以使用平台的 Message 类直接构造模版消息
        await weather.reject(city.template("你要查询的城市 {{city}} 暂不支持，请重新输入！"))
    city_weather = await get_weather(city_name)
    await weather.finish(city_weather)


# 返回结果
async def get_weather(city: str) -> str:
    return f"{city}的天气是..."
