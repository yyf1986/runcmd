#!/usr/bin/python

from handlers import index
from handlers import acceptkey
from handlers import listkey
from handlers import delkey
from handlers import down
from handlers import runsalt
from handlers import randompassword


urls = [
    (r'/', index.IndexHandler),
    (r'/acceptkey', acceptkey.AcceptHandler),
    (r'/delkey', delkey.DelHandler),
    (r'/listkey', listkey.ListHandler),
    (r'/down', down.DownHandler),
    (r'/salt', runsalt.IndexHandler),
    (r'/runsalt', runsalt.SaltHandler),
    (r'/randompasswd', randompassword.RandomHandler),
]
