# importing the required modules
import os
import redis
from rq import Worker, Queue, Connection

listen = ["high", "default", "low"]
# instantiating redistogo
# redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
port = os.getenv("REDIS_PORT", 6379)
username = os.getenv("REDIS_USER", "admin")
password = os.getenv("REDIS_PASSWORD", "admin")
host = os.getenv("REDIS_HOST", "localhost")

# creating a connnection
conn = redis.Redis(host=host, port=port, password=password, username=username)

# running when it is the main file
if __name__ == "__main__":
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
