#!/usr/bin/python3
""" Import app_views from api.v1.views """
from api.v1.views import app_views


@app_views.route("/status")
def status():
    """ Returns a JSON: 'status': 'OK' """
    return ({"Status": "OK"})
