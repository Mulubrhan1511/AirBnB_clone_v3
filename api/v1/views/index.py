#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from models import storage
from flask import Flask
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def get_status():
    return jsonify({"status": "OK"})

@app_views.route("/stats", methods=["GET"])
def get_stats():
    stats = {}
    for cls in storage.classes:
        stats[cls] = storage.count(cls)
    return jsonify(stats)
