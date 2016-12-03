# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:35:00 2016

@author: root
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../').replace('\\', '/'))

from user_agent import user_agent_list
from utils.generator_util import random_int
from config import *
from rq_jobs import *

import requests
from redis import Redis
from rq import Queue
import subprocess
import sys
import getopt
import signal
from bs4 import BeautifulSoup as bs

import logging
import time

class NeoSpider:
    
    def __init_(self):
        self.loginParam = LoginDict
        self.header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate, sdch',
                        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'User-Agent': '%s' % user_agent_list[random_int(len(user_agent_list)-1)],
                        'Referer': '%s' % (SpiderRules["main"])
                      }
        
        self.session = requests.Session()
        self.session.headers.update(self.header)
        self.nextUrl = ""
    
    def _login(self):
        
    
        resp = self.session.get(MySiteRules["main"])
        
        soup = bs(resp.text,'lxml')
        csrf_input_tag = soup.find("input",attrs={"name":"csrfmiddlewaretoken"})
        if csrf_input_tag == None:
            logging.error("can not found the csrf")
            return "", None
        MysiteLoginDict["csrfmiddlewaretoken"] = csrf_input_tag.attrs["value"]
        print MysiteLoginDict["csrfmiddlewaretoken"]
        
        #resp = session.post(resp.url, params={'ac':'account', 'op':'login'},
        #      data={'username':config["user"], 'userpwd':config["password"]})
        
        resp = self.session.post(resp.url, data=MysiteLoginDict)
        if resp.status_code != 200:
            logging.error("login failed errcode=%d",resp.status_code)
            return "", None
        
        if MySiteRules["start_url"]!="":
            resp = self.session.get(MySiteRules["start_url"])
            
        self.nextUrl = resp.url
        
    
    def startWorker(self):
        pass
    
    def stop(self):
        pass
    
    def loop(self):
        pass
    
    