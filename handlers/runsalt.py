#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import log

import tornado.web
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('salt.html')

def isexitgroup(group):
    import os
    cmd = "less /etc/salt/master.d/node.conf|grep -w %s:|wc -l" % group
    print cmd
    num = os.popen(cmd).readlines()[0].strip('\r\n')
    if int(num) == 1:
        return True
    else:
        return False

def run(tgtf,tgt,function,command):
    import salt.client
    rets = ""
    if tgtf == "NodeGroup":
        if isexitgroup(tgt):
            pass
        else:
            return "警告:%s组不存在!" % tgt
    local = salt.client.LocalClient()
    if function == "cmd.run":
        ret = local.cmd(tgt,function,[command],expr_form=tgtf.lower())
    elif function == "test.ping":
        ret = local.cmd(tgt,function,expr_form=tgtf.lower())
    if len(ret) == 0:
        rets = "警告:Target Format(%s) Target(%s)不存在!" % (tgtf,tgt)
    else:
        for key,value in ret.items():
            rets+= "机器IP"+key+"执行结果为:\n"+str(value)+"\n"
    return rets

class SaltHandler(tornado.web.RequestHandler):
    def post(self):
        result = {}
        tgtf = self.get_argument('format')
        tgts = self.get_argument('target')
        function = self.get_argument('functions')
        command = self.get_argument('cmd')
        rets = run(tgtf,tgts,function,command)
        result['result'] = rets
        loger = log.Log()
        loger.set_Name('saltrun')
        msg = "客户端IP:"+self.request.remote_ip+"针对于Target Format为"+tgtf+",Target机器为"+tgts+"执行函数"+function+"命令参数为"+command+"."
        loger.add_Msg(msg)
        self.write(json.dumps(result))
