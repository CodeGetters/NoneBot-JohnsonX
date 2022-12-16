# -*- coding = utf-8 -*-
# @Time: 2022/12/16 22:10
# @Author: JohonsonX
# @File: picture_01.py
# @SoftWare: PyCharm
from nonebot.adapters.onebot.v11 import Message, Bot, Event
from nonebot import on_keyword
from nonebot.typing import T_State
import requests

'''
随机返回二次元图片
API：https://api.btstu.cn/sjbz/api.php?lx=dongman&format=images
'''

catch_str = on_keyword({'二次元', '图片'})


@catch_str.handle()
async def send_img(bot: Bot, event: Event, state: T_State):
    API = 'https://api.btstu.cn/sjbz/api.php?lx=dongman'
    res = requests.get(API, timeout=1)
    msg = "[CQ:image,file=" + res.url + "]"
    await catch_str.finish(Message(f'{msg}'))
