from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

# Route 1: Welcome
@app.route("/")
def welcome():
    return "Welcome to the Coderco Challenge Redis visitor counter app!"

# Route 2: Counter
@app.route("/count")
def count():
    visits = r.incr("visits")
    return f"Visitor count: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)