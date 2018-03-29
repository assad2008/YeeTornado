# -*- coding: utf-8 -*-
# @Filename: run.py
# @Author: Yee
# @Email:  rlk002@gmail.com
# @Link: https://wj.pe
# @Date:   2018-03-20 11:57:27
# @Copyright: :copyright: (c)2018
# @Last Modified by:   Yee
# @Last Modified time: 2018-03-29 11:44:17


import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
from yee.settings.env import LOG_PATH

define("port", default=8899, help="miss port", type=int)
define("host", default="0.0.0.0", help="miss host")


settings = {
    "debug": True,
}


class MainApplication(tornado.web.Application):
    def __init__(self):
        from yee.handlers import routes as handlers
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    parse_command_line()
    app = MainApplication()
    app.listen(options.port, options.host)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
