#!/usr/bin/python3
""" Start your API """
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(err):
    """ Call storage.close """
    storage.close()


@app.errorhandler(404)
def not_found(err):
    """ Not Found Page """
    return (make_response(jsonify({"error": "Not found"}), 404))


if __name__ == "__main__":
    from os import getenv
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', '5000'))
    app.run(debug=True, host=host, port=port, threaded=True)
