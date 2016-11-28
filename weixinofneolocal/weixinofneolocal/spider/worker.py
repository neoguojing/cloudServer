# coding=utf-8
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../').replace('\\', '/'))

#from utils.neoconfig import NeoConfig
import redis
from rq import Worker, Queue, Connection
import multiprocessing
import logging
import signal

from config import RedisSetings
 
listen = ['high', 'default', 'low']

#tools = NeoConfig()
#temp = tools.loadFronJsonFile("./config.json")
#redis_url = 'redis://%s:%d' % (temp["redisaddr"], temp["port"])
redis_url = 'redis://%s:%d' % (RedisSetings["redisaddr"], RedisSetings["port"])
conn = redis.from_url(redis_url)

def signal_handler(signum,frame):
    for i in pid_list:
        os.kill(i,signal.SIGKILL)
    logging.info ("exit")
    sys.exit()

def worker():
    logging.info("a worker start")
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
 
pid_list=[]
signal.signal(signal.SIGINT,signal_handler)
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    for i in xrange(3):
        pool.apply_async(worker,)
    
    for i in multiprocessing.active_children():
        pid_list.append(i.pid)
    
    pid_list.append(os.getpid())
    pool.close()
    pool.join()
        