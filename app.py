from flask import Flask
from redis import Redis
import os

redis_port = os.environ.get('REDIS_PORT')

app = Flask(__name__)
redis = Redis(host="redis", port=redis_port)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello! I have been seen {0} times'.format(redis.get('hits'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
