# coding=utf-8
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
from pybloom import BloomFilter
import logging
import time

def md5(str):
    import hashlib
    import types
    
    if types(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest
    else:
        return ""

def LogIn():
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-us;q=0.5,en;q=0.3',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'User-Agent': '%s' % user_agent_list[random_int(len(user_agent_list)-1)],
            'Referer': '%s' % (MySiteRules["main"])
               }
    
    session = requests.Session()
    session.headers.update(headers)

    resp = session.get(MySiteRules["main"])
    
    soup = bs(resp.text,'lxml')
    csrf_input_tag = soup.find("input",attrs={"name":"csrfmiddlewaretoken"})
    if csrf_input_tag == None:
        logging.error("can not found the csrf")
        return "", None
    MysiteLoginDict["csrfmiddlewaretoken"] = csrf_input_tag.attrs["value"]
    print MysiteLoginDict["csrfmiddlewaretoken"]
    
    #resp = session.post(resp.url, params={'ac':'account', 'op':'login'},
    #      data={'username':config["user"], 'userpwd':config["password"]})
    
    resp = session.post(resp.url, data=MysiteLoginDict)
    if resp.status_code != 200:
        logging.error("login failed errcode=%d",resp.status_code)
        return "", None
    
    if MySiteRules["start_url"]!="":
        resp = session.get(MySiteRules["start_url"])
    
    return resp.url, session


def ProducerLoop(queue,url,session):
    
    next_url = url
    print next_url
    
    while True:
        
        pageContent = session.get(next_url)
        
        job = queue.enqueue(WorkerTaskCallback,pageContent.text)
        print job
        
        soup = bs(pageContent.text,'lxml')
        #next_url = soup.find(MySiteRules["rules"])
        
        #end condition
        if True:
            break
    logging.error("ProducerLoop ends")
    

class NeoBloomFilter:
    def __init__(self):
        self.bf = BloomFilter(capacity=10000, error_rate=0.0001)
        
    def isUrlExist(self, url):
        digest = md5(url)
        if digest == "":
            logging.error("md5() input is empty ")
            return True
        if digest in self.bf:
            return True
        else:
            self.bf.add(digest)
            return False


class Usage(Exception):
    def __init__(self,msg):
        self.msg = msg

def Exit(signum, frame):
    global worker
    if worker != None:
        logging.error("worker is being killing")
        #worker.kill()
    sys.exit()

def main(argv=None):
    global worker
    global session
    
    if argv==None:
        argv=sys.argv

    try:
        try:
            opts,args = getopt.getopt(argv[1:],"h",["help"])
            
            signal.signal(signal.SIGINT, Exit)
            signal.signal(signal.SIGTERM, Exit)
            
            #worker = subprocess.Popen("rq worker -c rq_worker&",shell=True)
            #worker.wait()
            
            logging.error("worker start success")
            
            start_url = ""
            if GlobleSettings["login"]:
                start_url,session = LogIn()
            
            redisQueue = Queue(connection=Redis(host=RedisSetings["redisaddr"], port=RedisSetings["port"], db=1))
            
            if session == None or start_url == "":
                logging.error("login err session is None ")
                return
            
            ProducerLoop(redisQueue,start_url,session)

            #while True:
                #print worker.poll()
                #time.sleep(1)

        except getopt.error,msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr,err.msg
        print >> sys.stderr, "for help use --help"
        return 2



worker = None
session = None

if __name__ == "__main__":
    sys.exit(main())








