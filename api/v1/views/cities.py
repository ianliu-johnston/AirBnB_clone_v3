#!/usr/bin/python3
"""
Cities module to interface with the API
"""
from api.v1.views import (app_views, City, State, storage)
from flask import (request, jsonify, abort)


@app_views.route('/states/<state_id>/cities',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def city_by_state(state_id=None):
    """
    Access the api call with on a state object to get its cities
    returns a 404 if not found.
    POST alala
    Defaults is to return the state object.
    """
    if state_id not in storage.all('State'):
        print("Invalid ID")
        abort(404)

    if request.method == 'POST':
        post_obj = request.get_json()
        if post_obj is None:
            return("Not a JSON", 400)
        if 'name' not in post_obj:
            return("Missing name", 400)
        new_obj = City(**post_obj)
        new_obj.state_id = state_id
        new_obj.save()
        return(jsonify(new_obj.to_json()), 201)

    """Default: GET request returns the object in json form"""
    all_cities = storage.get('State', state_id).cities
    rtn_json = []
    for city in all_cities:
        rtn_json.append(city.to_json())
    return(jsonify(rtn_json))


"""
@app_views.route('/cities/<city_id>',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def all_cities():
    Adds new State objects, if provided with a name parameter in a POST request
    Default is to Returns a list of all states in json format for GET requests
    if request.method == 'POST':
        posted_obj = request.get_json()
        if posted_obj is None:
            return("Not a JSON", 400)
        if 'name' not in posted_obj:
            return("Missing name", 400)
        new_obj = State(**posted_obj)
        storage.save()
        return(jsonify(new_obj.to_json()), 201)

    rtn_json = []
    all_obj = storage.all('State')
    for instance in all_obj:
        rtn_json.append(all_obj[instance].to_json())
    return (jsonify(rtn_json))




    if request.method == 'DELETE':
        storage.delete(storage.get('State', state_id))
        storage.save()
        return(jsonify({}))

    if request.method == 'PUT':
        put_obj = request.get_json()
        if put_obj is None:
            return("Not a JSON", 400)
        instance = storage.get('State', state_id)
        for attrib in put_obj:
            setattr(instance, attrib, put_obj[attrib])
        instance.save()
        return(jsonify(instance.to_json()))
"""
