# importing the required modules
import os
import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']
# instantiating redistogo
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

# creating a connnection
conn = redis.from_url(redis_url)

# running when it is the main file
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
