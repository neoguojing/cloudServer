# coding=utf-8
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../').replace('\\', '/'))

from user_agent import user_agent_list
from utils.generator_util import random_int
from config import *

import requests
from redis import Redis
from rq import Queue
import subprocess
import sys
import getopt
import signal
from bs4 import BeautifulSoup as bs



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
    print resp.url,resp.status_code
    
    soup = bs(resp.text,'lxml')
    MysiteLoginDict["csrfmiddlewaretoken"] = soup.find("input",attrs={"name":"csrfmiddlewaretoken"}).attrs["value"]
    print MysiteLoginDict["csrfmiddlewaretoken"]
    
    #resp = session.post(resp.url, params={'ac':'account', 'op':'login'},
    #      data={'username':config["user"], 'userpwd':config["password"]})
    
    resp = session.post(resp.url, data=MysiteLoginDict)
    print resp.url,resp.status_code 
    print resp.text
    
    if MySiteRules["start_url"]!="":
        resp = session.get(MySiteRules["start_url"])
    
    return resp.url, session

def WorkerTaskCallback(html):
    #what data do I need
    
    

def ProducerLoop(queue,url,session):
    
    next_url = url
    while True:
        #end condition
        if False:
            break
        
        pageContent = session.get(next_url)
        
        queue.enqueue(WorkerTaskCallback,pageContent.text)
        
        soup = bs(pageContent.text,'lxml')
        next_url = soup.find(MySiteRules["rules"])


class Usage(Exception):
    def __init__(self,msg):
        self.msg = msg

def Exit(signum, frame):
    if worker != None:
        worker.kill()
    sys.exit()


def main(argv=None):
    if argv==None:
        argv=sys.argv

    try:
        try:
            opts,args = getopt.getopt(argv[1:],"h",["help"])

            signal.signal(signal.SIGINT, Exit)
            signal.signal(signal.SIGTERM, Exit)

            worker = subprocess.Popen("rq worker",shell=True)
            worker.wait()
            
            start_url = ""
            session = None
            if GlobleSettings["login"]:
                start_url,LogIn()
            
            redisQueue = Queue(connection=Redis(host=RedisSetings["redisaddr"], port=RedisSetings["port"], db=1))
            
            ProducerLoop(redisQueue,)

            while True:
                worker.poll()
                
                

        except getopt.error,msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr,err.msg
        print >> sys.stderr, "for help use --help"
        return 2



if __name__ == "__main__":
    sys.exit(main())








