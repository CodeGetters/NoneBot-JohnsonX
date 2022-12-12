# -*- coding = utf-8 -*-
# @Time: 2022/12/11 20:11
# @Author: JohonsonX
# @File: today.py
# @SoftWare: PyCharm

from nonebot import on_keyword,on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,MessageEvent, Bot, Message, Event
import requests

'''
疫情查询 调用API：http://api.yanxi520.cn/api/virus.php?msg=
命令：#疫情+城市
'''

covid = on_keyword({'疫情'})
# covid=on_regex(pattern='^{疫情}')

@covid.handle()
async def query(bot: Bot, event: GroupMessageEvent|MessageEvent, state: T_State):
    get_city = str(event.get_message()).strip()
    get_city = get_city.strip('疫情')
    url = f'http://api.yanxi520.cn/api/virus.php?msg={get_city}'
    get_data = requests.get(url)
    msg = get_data.text
    html = '{br}'
    n = '\n'
    quezhen = '目前'
    lj = '累计'

    if html in msg:
        msg = msg.replace(html, n)
    elif quezhen in msg:
        msg = msg.replace(quezhen, lj)
    await covid.finish(Message(f'{msg}'))