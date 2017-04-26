#!/usr/bin/python3
"""
States module to interface with the API
"""
from api.v1.views import (app_views, State, storage)
from flask import (request, jsonify, abort)


@app_views.route('/states',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def all_states():
    """
    Adds new State objects, if provided with a name parameter in a POST request
    Default is to Returns a list of all states in json format for GET requests
    """
    if request.method == 'POST':
        try:
            posted_obj = request.get_json()
        except:
            return("Not a JSON", 400)
        if 'name' not in posted_obj:
            return("Missing Name", 400)
        new_obj = State(**posted_obj)
        storage.save()
        return(jsonify(new_obj.to_json()), 201)

    rtn_json = []
    all_obj = storage.all('State')
    for instance in all_obj:
        rtn_json.append(all_obj[instance].to_json())
    return (jsonify(rtn_json))


@app_views.route('/states/<state_id>',
                 methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def state_by_id(state_id=None):
    """
    Access the api call with on a specific state object
    returns a 404 if not found.
    Delete method removes the object
    Defaults is to return the state object.
    """
    if state_id not in storage.all('State'):
        abort(404)

    if request.method == 'DELETE':
        storage.delete(storage.get('State', state_id))
        return(jsonify({}))

    if request.method == 'PUT':
        try:
            put_obj = request.get_json()
        except:
            return("Not a JSON", 400)
        instance = storage.get('State', state_id)
        for attrib in put_obj:
            setattr(instance, attrib, put_obj[attrib])
        instance.save()
        return(jsonify(instance.to_json()))

    """Default: GET request returns the object in json form"""
    instance = storage.get('State', state_id)
    return(jsonify(instance.to_json()))
"""
Update the State object with all key-value pairs of the dictionary.
Ignore keys: id, created_at and updated_at
"""
