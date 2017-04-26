#!/usr/bin/python3
"""
States module to interface with the API
"""
from api.v1.views import app_views
from flask import (request, jsonify, abort, request)
from models import storage


@app_views.route('/states', methods=['GET', 'POST'])
def all_states():
    """
    Returns a list of all states.
    """
    states_dict = {}
    for item in storage.all():
#        states_dict.update(item)
        print(item)
    return("Hello!")


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def state_by_id(state_id):
    """
    Gets a state at state_id.
    returns a 404 if not found.
    """
    if state_id not in storage.all():
        abort(404)
    if request.method == 'DELETE':
        storage.delete(storage.get(storage.available_classes['State'], state_id))
        return(jsonify({}, 200))
    if request.method == 'PUT':
        return("lala")

    json_rtn = {}
    all_objs = storage.get(storage.available_classes['State'], state_id)
    print(all_objs)
    for key, value in all_objs:
        json_rtn.update({key: value})
    return(jsonify(json_rtn))
