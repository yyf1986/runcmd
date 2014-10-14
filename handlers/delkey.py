#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.web

def delkey(ip):
    import salt.config
    import salt.key
    __opts__ = salt.config.client_config('/etc/salt/master')
    key = salt.key.Key(__opts__)
    keys = key.list_keys()
    minions = keys['minions']
    if ip in minions:
        key.delete_key(ip)
        msg = "Delete %s sucess!" % ip
    else:
        msg = "%s is not in minions!" % ip
    return msg

class DelHandler(tornado.web.RequestHandler):
    def get(self):
        result = {}
        ip = self.get_argument('ip')
        result['result'] = delkey(ip)
        self.write(json.dumps(result))
