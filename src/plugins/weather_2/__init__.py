# -*- coding = utf-8 -*-
# @Time: 2022/12/13 21:28
# @Author: JohonsonX
# @File: __init__.py
# @SoftWare: PyCharm
import json
# 引入事件响应器模块
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.adapters.onebot.v11 import Bot, Message
# 天气查询模块
from .weather_data import get_data, get_future
# emoji模块(表情)
import emoji

'''
最近几天的天气
命令：/天气02
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
    '欢迎来到天气查询功能:sparkles:\n请问您需要查询的城市天气是...\n查询示例：北京-北京'
)


@weather.got("city", prompt=welcome)
async def handle_city(city: Message = Arg(), city_name_list: str = ArgPlainText("city")):
    path = r'D:\软件类存储地\桌面\代码合集\python\聊天机器人\JohnsonX\src\plugins\weather_2\city.json'
    # 读取city.json文件
    with open(path, 'r', encoding='utf8') as f:
        data = json.load(f)
    # 如果参数不符合，重新输入
    if city_name_list.find('-') == -1:
        await weather.reject(city.template('输入格式出错了，请对比上面的示例重新输入吧！'))
    province = city_name_list.split('-')[0]
    city_name = city_name_list.split('-')[1]
    if city_name not in data[province]:
        # 错误消息处理
        await weather.reject(city.template('你要查询的城市 {city} 暂不支持，请重新检查再输入吧！'))
    # 获得天气信息
    infor = get_data(city_name)
    infor_future = get_future(city_name)
    if type(infor or infor_future) == str:
        results = "接口出错了，请稍后再试！"
    else:
        results = f"{city_name}的天气为：\r\n目前：" + infor[0] + "  温度：" + infor[1] + "\r\n明日：" + infor_future[
            0] + "  最高温度为：" + infor_future[1] + "  最低温度为：" + infor_future[2] + "  降水概率为：" + infor_future[
                      3]
    await weather.finish(results)
