"""Module for Intializing APP"""
import os

from flask import Flask
from . import api, graphql


def create_app(test_config=None):
    """Function to create API"""
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # Configuration goes here
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    app.register_blueprint(api.bp)
    app.register_blueprint(graphql.bp)

    return app
