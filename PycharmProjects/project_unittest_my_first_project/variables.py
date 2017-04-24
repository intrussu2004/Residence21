# coding=utf-8
__author__ = 'eharcil'

import os
import sys
from selenium import webdriver
from datetime import datetime

url = "http://21residence-politehnica.ro"
driver = webdriver.Firefox()
#driver = webdriver.Ie("C:\Python27\IEDriverServer.exe")
#driver = webdriver.Chrome("C:\Python27\chromedriver.exe")

daily_directory_for_screenshots = r'C:\Users\eharcil\PycharmProjects\project_unittest_my_first_project\screenshots\\'
#daily_directory_for_logs = r'C:\Users\eharcil\PycharmProjects\project_unittest_my_first_project\logs\\'
today = datetime.now().strftime('%d-%b-%Y')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': (u'%(asctime)s [%(process)d] [%(levelname)s] ' +
                       '%(module)s.%(funcName)s::%(lineno)s '
                       '%(message)s'),
        },
        'simple': {
            'format': u'%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'C:\Users\eharcil\PycharmProjects\project_unittest_my_first_project\logs\\'+today+' '+'test.log',
            'maxBytes': '16777216', # 16megabytes
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        }
    }
}