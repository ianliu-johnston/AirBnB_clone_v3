#!/usr/bin/python3
"""
landing page for api
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status')
def app_status():
    return(jsonify(status="OK"))

@app_views.route('/stats')
def app_get_count():
    tojson = {}
    for cls in storage.available_classes:
        tojson.update({ cls: storage.count(cls) })
    return(jsonify(tojson))
