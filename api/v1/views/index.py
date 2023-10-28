#!/usr/bin/python3
""" Import app_views from api.v1.views """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """ Returns a JSON: 'status': 'OK' """
    return jsonify(status="OK")


@app_views.route("/stats", strict_slashes=False)
def stats():
    """ Retrieves the number of each objects by type """
    return (make_response(jsonify(
            amenities=storage.count('Amenities'),
            cities=storage.count('Cities'),
            places=storage.count('Places'),
            reviews=storage.count('Reviews'),
            states=storage.count('States'),
            users=storage.count('Users')
            )))


if __name__ == "__main__":
    pass
