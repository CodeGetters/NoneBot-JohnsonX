# -*- coding = utf-8 -*-
# @Time: 2022/12/11 21:05
# @Author: JohonsonX
# @File: randomWord.py
# @SoftWare: PyCharm
import requests
from nonebot import on_keyword, on_regex

from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent, Bot, Message

'''
随机一言
API：'http://api.weijieyue.cn/api/yy/api.php
'''
# randomWord = on_keyword('{随机一言}')
randomWord = on_regex(pattern='^今日诗词')


@randomWord.handle()
async def ranwo(bot: Bot, event: GroupMessageEvent | PrivateMessageEvent, state: T_State):
    lovelive_send = await xi()
    await randomWord.send(Message(lovelive_send))


async def xi():
    # url = "https://v.api.aa1.cn/api/yiyan/index.php"
    # url = "https://v2.jinrishici.com/one.svg"
    url = "https://v1.jinrishici.com/rensheng.txt"
    hua = requests.get(url=url)
    data = hua.text
    return data
