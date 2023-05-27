#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host, int(port), threaded=True)
