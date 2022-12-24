# -*- coding = utf-8 -*-
# @Time: 2022/12/24 21:32
# @Author: JohonsonX
# @File: loveTalk.py
# @SoftWare: PyCharm

# 正则
from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Message, MessageEvent, Bot
import requests

'''
情话 调用API https://api.mcloc.cn/love?type=json
命令：情话
'''

loveTalk = on_regex(pattern=r'^情话$')


@loveTalk.handle()
async def talk(bot: Bot, event: MessageEvent, state: T_State):
    saying = await get_talk()
    await loveTalk.send(Message(saying))


async def get_talk():
    url = 'https://api.mcloc.cn/love'
    result = requests.get(url=url, timeout=30)
    result_text = result.text
    return result_text
