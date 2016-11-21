# coding=utf-8
from utils.neoconfig import NeoConfig
import os
import redis
from rq import Worker, Queue, Connection
 
listen = ['high', 'default', 'low']

tools = NeoConfig()
temp = tools.loadFronJsonFile("./config.json")
redis_url = 'redis://%s:%d' % (temp[redisaddr], temp["port"])
 
conn = redis.from_url(redis_url)
 
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
