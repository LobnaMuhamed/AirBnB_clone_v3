#!/usr/bin/python3
""" Import app_views from api.v1.views """
from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """ Returns a JSON: 'status': 'OK' """
    return jsonify(status="OK")


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """ Retrieves the number of each objects by type """
    all_stats = {
                "amenities": storage.count(Amenity),
                "cities": storage.count(City),
                "places": storage.count(Place),
                "reviews": storage.count(Review),
                "states": storage.count(State),
                "users": storage.count(User)
                }
    return (make_response(jsonify(all_stats)))
