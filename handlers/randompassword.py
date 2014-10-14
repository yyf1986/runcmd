#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.web


def randpasswd():
    import random
    a = ""
    for j in random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', \
                        'i', 'j', 'k', 'A', 'B', 'C', 'D', 'E', 'F', 'G', '1', '2', '3','4','5'], 8):
        a += j
    return a

class RandomHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(randpasswd())
