#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
'''
Created on 2014-2-26

@author: 11113072
'''
import logging
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time

rq = time.strftime('%Y%m%d',time.localtime(time.time()))
logsetting = {
           'logpath':'./logs/',
           'level':'info',
           'filename':rq+'.log'
           }

class Log(object):
    ''' '''
    def __init__(self,fn=""):
        self.path = logsetting['logpath']
        self.filename = fn+logsetting['filename']
        self.level = logsetting['level']
    def set_Name(self,name):
        self.name = name
    def set_Level(self,level):
        self.level = level
    def set_Path(self,path):
        self.path = path
    def set_Filename(self,filename):
        self.filename = filename
    def add_Msg(self,msg):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)
        if os.path.exists(self.path):
            logfile = self.path+self.filename
            fh = logging.FileHandler(logfile)
        else:
            fh = logging.FileHandler(self.filename)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        if self.level.upper() == "INFO":
            logger.info(msg)
        elif self.level.upper() == "WARNING":
            logger.warning(msg)
        elif self.level.upper() == "ERROR":
            logger.error(msg)
        else:
            logger.debug(msg)
        fh.close()
        logger.removeHandler(fh)
