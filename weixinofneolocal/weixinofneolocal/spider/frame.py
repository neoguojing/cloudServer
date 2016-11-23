# coding=utf-8
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../').replace('\\', '/'))

from utils.neoconfig import NeoConfig
import requests
from redis import Redis
from rq import Queue
import subprocess
import sys
import getopt
import signal


class SpiderConfig:

    def __init__(self,user,pwd,redis_ip,port,main,*rules):
        self.user = user
        self.password = pwd
        self.redisaddr = redis_ip
        self.port = port
        self.main = main
        self.rules = rules


config = None
session = None
worker = None

def LoadConfig():
    tools = NeoConfig()
    temp = tools.loadFronJsonFile("./config.json")
    config = SpiderConfig(temp["username"],temp["password"],temp["redisaddr"],temp["port"],temp["main"],temp["rules"])


def LogIn():
    if config == None:
        return
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, compress',
            'Accept-Language': 'en-us;q=0.5,en;q=0.3',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
            'Referer':config.main
               }

    session = requests.Session()
    session.headers.update(headers)

    resp = session.get(config.main)
    resp = session.post(resp.url, params={'ac':'account', 'op':'login'},
           data={'username':config.user, 'userpwd':config.password})

    return resp.url

def taskCallback(url):
    resp = session.get(url,params={'ac':'common', 'op':'usersign'})


def InitRQ(url):
     redisQueue = Queue(connection=Redis(host=config.redisaddr, port=config.port, db=1))
     redisQueue.enqueue(taskCallback,url)

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








