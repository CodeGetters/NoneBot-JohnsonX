# -*- coding = utf-8 -*-
# @Time: 2022/12/10 21:27
# @Author: JohonsonX
# @File: welcome.py
# @SoftWare: PyCharm

# 通知事件响应器
from nonebot import on_notice
# 事件处理状态模块
from nonebot.typing import T_State
# GroupIncreaseNoticeEvent:群成员增加事件
# GroupDecreaseNoticeEvent:群成员减少事件
from nonebot.adapters.onebot.v11 import Bot, Message, GroupDecreaseNoticeEvent, GroupIncreaseNoticeEvent

# 注册通知事件响应器
welcome = on_notice()


# 群友加群
# 事件处理起点
@welcome.handle()
async def _(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    # 获取新进群群友的qq号
    user = event.get_user_id()
    # go-cqhttp：@新进群的群友
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '/n' + '欢迎新朋友的加入！'
    msg = Message(msg)
    await welcome.finish(message=msg)


# 群友退群
# 事件处理起点
@welcome.handle()
async def _(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '\n' + '一位朋友离我们而去！'
    msg = Message(msg)
    await welcome.finish(message=msg)
