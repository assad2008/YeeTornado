#/usr/bin/python
# coding=utf-8

from peewee import Model
from peewee_async import PooledMySQLDatabase
from yee.settings.db import *

db_master = PooledMySQLDatabase(DB_NAME, host=DB_HOST, port=DB_PORT, user=DB_USER,
                                password=DB_PASSWD, charset='utf8mb4')
db_master.connect()


class BaseModel(Model):

    class Meta:
        database = db_master
