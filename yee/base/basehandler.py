# -*- coding: utf-8 -*-
# @Filename: basehandler.py
# @Author: Yee
# @Email:  rlk002@gmail.com
# @Link: https://wj.pe
# @Date:   2018-03-20 14:30:32
# @Copyright: :copyright: (c)2018
# @Last Modified by:   Yee
# @Last Modified time: 2018-03-29 11:45:25


import tornado.web
from tornado.escape import json_encode, json_decode
from yee.libs.functions import debug

from json import JSONDecodeError
DEFAULT_JSON_ARGUMENT = object()


class BaseHandler(tornado.web.RequestHandler):

    def prepare(self):
        return super().prepare()

    def debug(self, string):
        debug(string)

    def jsonecho(self, reponse={}, code=0, tips='success'):
        response_dict = {}
        if code == 0:
            response_dict["code"] = 0
            response_dict["msg"] = tips
            if reponse != {}:
                response_dict["result"] = reponse
        else:
            response_dict["code"] = '-' + str(abs(code))
            response_dict["msg"] = tips
            if reponse != {}:
                response_dict["result"] = reponse
        redata = json_encode(response_dict)
        self.debug(redata)
        self.write(redata)

    def on_finish(self):
        pass


class RequestMixin:

    def __init__(self):
        pass


class JsonBodyMixin:
    @property
    def json(self):
        if not hasattr(self, '_json'):
            mimetype = self.request.headers['Content-Type'].lower()
            if mimetype.startswith('application/json'):
                encoding = 'utf-8'
                if mimetype[16:].startswith("; charset="):
                    encoding = mimetype[26:]
                try:
                    data = self.request.body.decode(encoding).strip()
                    self._json = json_decode(data) if data else {}
                except (LookupError, UnicodeDecodeError, JSONDecodeError):
                    self._json = {}
            else:
                self._json = {}
        return self._json

    def get_json_arg(self, name, default=DEFAULT_JSON_ARGUMENT):
        if name not in self.json:
            if default is DEFAULT_JSON_ARGUMENT:
                raise JSONHTTPError(400, "missing_arguments")
            return default
        return self.json[name]
