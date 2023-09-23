"""Module to provide api endpoints"""
from flask import Blueprint
from strawberry.flask.views import AsyncGraphQLView

from . import schema

bp = Blueprint("graphql", __name__)

bp.add_url_rule(
    "/graphql",
    view_func=AsyncGraphQLView.as_view(
        "graphql_view", schema=schema.schema, graphiql=True
    ),
)
