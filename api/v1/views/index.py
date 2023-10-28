#!/usr/bin/python3
""" Import app_views from api.v1.views """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """ Returns a JSON: 'status': 'OK' """
    return jsonify(status="OK")


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """ Retrieves the number of each objects by type """
    all_stats = {
                "amenities": storage.count('Amenities'),
                "cities": storage.count('Cities'),
                "places": storage.count('Places'),
                "reviews": storage.count('Reviews'),
                "states": storage.count('States'),
                "users": storage.count('Users')
                }
    return (jsonify(all_stats))


if __name__ == "__main__":
    pass
