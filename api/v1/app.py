#!/usr/bin/python3
"""
Module to register blueprints and run the flask server
in preparation for api calls
"""
from flask import Flask
from models import engine
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_flask():
    storage.close


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port)
