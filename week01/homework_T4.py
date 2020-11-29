#!/usr/local/env python

import logging
import time
import os


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def logset(path):
    logname = path + '/access.log'
    logging.basicConfig(filename=logname, level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M%S',
                        format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')

def queryTime():
    logging.info('info message')
    return time.strftime('%Y-%m-%d %X', time.localtime())


if __name__ == '__main__':
    path = '/var/log/python-' + time.strftime('%Y-%m-%d', time.localtime())
    #path = '/Users/qiulibo/Documents/python训练营/Python005-01/week01-' + time.strftime('%Y-%m-%d', time.localtime())
    mkdir(path)
    logset(path)
    queryTime()
