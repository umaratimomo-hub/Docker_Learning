from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

# Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

# Route 1: Welcome
@app.route("/")
def welcome():
    return render_template("index.html")

# Route 2: Counter
@app.route("/count")
def count():
    visits = r.incr("visits")
    return render_template("count.html", visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)