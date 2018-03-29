# -*- coding: utf-8 -*-
# @Filename: index.py
# @Author: Yee
# @Email:  rlk002@gmail.com
# @Link: https://wj.pe
# @Date:   2018-03-20 14:37:09
# @Copyright: :copyright: (c)2018
# @Last Modified by:   Yee
# @Last Modified time: 2018-03-29 12:10:38


from yee.base.basehandler import BaseHandler, RequestMixin, JsonBodyMixin

from yee.models.users import usersModel
from playhouse.shortcuts import model_to_dict


class IndexHandler(BaseHandler, RequestMixin, JsonBodyMixin):

    def initialize(self):
        super(BaseHandler, self).initialize()
        self.um = usersModel()

    async def get(self):
        user = await self.um.get_user_by_user_id("dkjsa")
        self.jsonecho(model_to_dict(user))
        return


routes = [
    (r"/", IndexHandler),
]
