#!/usr/bin/python

import tornado.web
import os.path

from urls import urls

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = tornado.web.Application(urls, **settings)
