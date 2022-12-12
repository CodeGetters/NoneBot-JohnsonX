# -*- coding = utf-8 -*-
# @Time: 2022/12/11 20:54
# @Author: JohonsonX
# @File: dayWorld.py
# @SoftWare: PyCharm

from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent, Bot, Message
import requests

'''
每日一言 调用API：https://api.juncikeji.xyz/api/mryy.php
命令：每日一言
'''
mryy = on_regex(pattern=r'^每日一言$')


# mryy = on_keyword('{每日一言}')


@mryy.handle()
async def yy(bot: Bot, event: GroupMessageEvent | PrivateMessageEvent, state: T_State):
    msg = await get_yy()
    await mryy.send(Message(msg))


async def get_yy():
    url = 'https://api.juncikeji.xyz/api/mryy.php'
    get_data = requests.get(url=url, timeout=20)
    get_text = get_data.text
    return get_text
