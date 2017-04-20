#!/usr/bin/python3
"""
landing page for api
"""
from api.v1.views import app_views
from flask import Flask, jsonify
import models


@app_views.route('/status')
def app_status():
    return(jsonify(status=OK))

@app_views.route('/api/v1/stats')
def status():

    return(models.storage.count())
