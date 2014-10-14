#!/usr/bin/python

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        #query = self.get_argument('ip')
        #a = self.get_argument('a')
        self.render('index.html')
