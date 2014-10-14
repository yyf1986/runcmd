#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.web


def listdown():
    import salt.key
    import salt.client
    import salt.config
    __opts__ = salt.config.client_config('/etc/salt/master')
    client = salt.client.LocalClient()
    minions = client.cmd('*', 'test.ping', timeout=30)
    key = salt.key.Key(__opts__)
    keys = key.list_keys()
    ret = {}
    #ret['up'] = sorted(minions)
    ret['down'] = sorted(set(keys['minions']) - set(minions))
    return ret

class DownHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(listdown()))
