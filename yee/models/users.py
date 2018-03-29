# -*- coding: utf-8 -*-
# @Filename: users.py
# @Author: Yee
# @Email:  rlk002@gmail.com
# @Link: https://wj.pe
# @Date:   2018-03-26 16:04:32
# @Copyright: :copyright: (c)2018
# @Last Modified by:   Yee
# @Last Modified time: 2018-03-29 12:09:51

import time
from yee.models.schemas import Users


class usersModel(object):

    def __init__(self):
        self.tab = Users

    async def get_user(self, id):
        try:
            return self.tab.get(self.tab.id == id)
        except:
            return None

    async def get_user_by_user_id(self, user_id):
        try:
            return self.tab.get(self.tab.user_id == user_id)
        except:
            return None

    async def create_user(self, user_id, kwagrs):
        user = await self.tab.create(
            user_id=user_id,
            payment_address=kwagrs.get("payment_address") or "",
            username=kwagrs.get("username") or "",
            nickname=kwagrs.get("nickname") or "",
            avatar=kwagrs.get("avatar") or "",
            about=kwagrs.get("about") or "",
            islocked=kwagrs.get("islocked") or "0",
            create_at=kwagrs.get("create_at") or int(time.time()),
            update_at=kwagrs.get("update_at") or int(time.time())
        )
        return user.id or None

    async def update_user(user_id, user):
        pass
