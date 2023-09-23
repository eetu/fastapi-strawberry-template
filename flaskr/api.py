"""Module to provide api endpoints"""
from flask import Blueprint, jsonify, Response

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("")
def index() -> Response:
    """Function for returning hello world!"""
    return jsonify({"message": "hello world!"})
