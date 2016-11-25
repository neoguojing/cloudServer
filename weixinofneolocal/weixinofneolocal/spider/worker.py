# coding=utf-8
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../').replace('\\', '/'))

#from utils.neoconfig import NeoConfig
import redis
from rq import Worker, Queue, Connection

from config import RedisSetings
 
listen = ['high', 'default', 'low']

#tools = NeoConfig()
#temp = tools.loadFronJsonFile("./config.json")
#redis_url = 'redis://%s:%d' % (temp["redisaddr"], temp["port"])
redis_url = 'redis://%s:%d' % (RedisSetings["redisaddr"], RedisSetings["port"])
conn = redis.from_url(redis_url)
 
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
