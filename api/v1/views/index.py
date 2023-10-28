#!/usr/bin/python3
""" Import app_views from api.v1.views """
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """ Returns a JSON: 'status': 'OK' """
    return jsonify(Status="OK")


if __name__ == "__main__":
    pass
