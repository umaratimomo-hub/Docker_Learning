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

# Route 2:
@app.route("/architecture")
def architecture():
    return render_template("architecture.html")

# Route 3:
@app.route("/how-it-works")
def how_it_works():
    return render_template("how_it_works.html")

# Route 4:
@app.route("/technology")
def technology():
    return render_template("technology.html")

# Route 5:
@app.route("/project")
def project():
    return render_template("project.html")

# Route 6: Counter
@app.route("/count")
def count():
    visits = r.incr("visits")
    return render_template("count.html", visits=visits)

# Route 7:
@app.route("/future")
def future():
    return render_template("future.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)