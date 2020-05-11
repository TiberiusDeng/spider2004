import redis
from random import choice

pool = redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=10)
conn = redis.Redis(connection_pool=pool,decode_responses=True)
print(conn.lindex("proxies",1))