"""Module to provide api endpoints"""
from flask import Blueprint
from strawberry.flask.views import AsyncGraphQLView
import strawberry


def get_message() -> str:
    """Get message function"""
    return "Hello world!"


@strawberry.type
class Query:
    """Query"""

    message: str = strawberry.field(resolver=get_message)


schema = strawberry.Schema(query=Query)

bp = Blueprint("graphql", __name__)

bp.add_url_rule(
    "/graphql",
    view_func=AsyncGraphQLView.as_view("graphql_view", schema=schema, graphiql=True),
)
