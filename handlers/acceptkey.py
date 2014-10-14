#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.web

def acceptkey(ip):
    import salt.config
    import salt.key
    __opts__ = salt.config.client_config('/etc/salt/master')
    key = salt.key.Key(__opts__)
    keys = key.list_keys()
    minionpres = keys['minions_pre']
    if ip in minionpres:
        key.accept(ip)
        msg = "Add "+ip+" sucess!"
    else:
        msg = ip+" is not in minions_pre!"
    return msg

class AcceptHandler(tornado.web.RequestHandler):
    def get(self):
        result = {}
        ip = self.get_argument('ip')
        result['result'] = acceptkey(ip)
        self.write(json.dumps(result))
