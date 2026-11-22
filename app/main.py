import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)
store = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True, socket_connect_timeout=2)

@app.get("/api/stats")
def stats():
    count = store.incr("demo:requests")
    return jsonify(requests=count, app="portfolio-api", datastore="redis", status="healthy")

@app.get("/health")
def health():
    store.ping()
    return jsonify(status="healthy", datastore="reachable")
