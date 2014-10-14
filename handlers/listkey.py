#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.web

def listkey():
    import salt.config
    import salt.key
    __opts__ = salt.config.client_config('/etc/salt/master')
    key = salt.key.Key(__opts__)
    keys = key.list_keys()
    minionpres = keys['minions_pre']
    ret = ""
    for ip in minionpres:
        ret += ip+","
    return ret

class ListHandler(tornado.web.RequestHandler):
    def get(self):
        result = {}
        result['result'] = listkey()
        self.write(json.dumps(result))
