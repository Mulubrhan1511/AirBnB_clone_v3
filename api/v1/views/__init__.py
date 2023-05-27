#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
