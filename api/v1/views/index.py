#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "OK"})
