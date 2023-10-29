#!/usr/bin/python3
""" Create a new view for State objects that handles
    all default RESTFul API actions
"""
from models.state import State
from flask import Flask, jsonify, make_response, abort, request
from api.v1.views import app_views
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """ Retrieves the list of all State objects """
    states = storage.all(State).values()
    state_list = [state.to_dict() for state in states]
    return (jsonify(state_list))


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ Retrieves a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return (jsonify(state.to_dict()))


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ Deletes a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    storage.delete(state)
    storage.save()
    return (make_response(jsonify({}), 200))


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """ Creates a State"""
    req = request.get_json()

    if req is None:
        abort(400, "Not a JSON")
    if 'name' not in req:
        abort(400, "Missing name")

    state = State(**req)
    state.save()
    return (make_response(jsonify(state.to_dict()), 201))


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """ Creates a State"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    req = request.get_json()
    obj = {}

    if req is None:
        abort(400, "Not a JSON")

    for key, val in req.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, val)

    state.save()
    return (make_response(jsonify(state.to_dict()), 200))
