# -*- coding: utf-8 -*-
# @Filename: schemas.py
# @Author: Yee
# @Email:  rlk002@gmail.com
# @Link: https://wj.pe
# @Date:   2018-03-29 11:26:26
# @Copyright: :copyright: (c)2018
# @Last Modified by:   Yee
# @Last Modified time: 2018-03-29 12:04:23

from peewee import *
from yee.models import BaseModel


class Users(BaseModel):

    class Meta:
        db_table = "users"

    id = IntegerField(primary_key=True)
    user_id = CharField()
    payment_address = CharField(null=False)
    username = CharField()
    nickname = CharField()
    avatar = CharField()
    about = CharField()
    islocked = IntegerField(default=0)
    create_at = IntegerField(default=0)
    update_at = IntegerField(default=0)
