#!/usr/bin/python3
""" Create a new view for Amenity objects that handles
    all default RESTFul API actions
"""
from models.amenity import Amenity
from flask import Flask, jsonify, make_response, abort, request
from api.v1.views import app_views
from models import storage


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """ Retrieves the list of all Amenity objects """
    amenities = storage.all(Amenity).values()
    amenity_list = [amenity.to_dict() for amenity in amenities]
    return (jsonify(amenity_list))


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """ Retrieves a Amenity object """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return (jsonify(amenity.to_dict()))


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """ Deletes a Amenity object """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    storage.delete(amenity)
    storage.save()
    return (make_response(jsonify({}), 200))


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
    """ Creates a Amenity"""
    req = request.get_json()

    if req is None:
        abort(400, "Not a JSON")
    if 'name' not in req:
        abort(400, "Missing name")

    amenity = Amenity(**req)
    amenity.save()
    return (make_response(jsonify(amenity.to_dict()), 201))


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def put_amenity(amenity_id):
    """ Creates a Amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    req = request.get_json()
    obj = {}

    if req is None:
        abort(400, "Not a JSON")

    for key, val in req.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, val)

    amenity.save()
    return (make_response(jsonify(amenity.to_dict()), 200))
