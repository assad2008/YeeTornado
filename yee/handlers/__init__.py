# -*- coding: utf-8 -*-
# @Filename: __init__.py
# @Author: Yee
# @Email:  rlk002@gmail.com
# @Link: https://wj.pe
# @Date:   2018-03-29 11:22:54
# @Copyright: :copyright: (c)2018
# @Last Modified by:   Yee
# @Last Modified time: 2018-03-29 11:43:23


from yee.handlers import index

routes = []

routes.extend(index.routes)
