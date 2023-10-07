"""Module to provide graphql schema"""
import strawberry


def get_message() -> str:
    """Get message function"""
    return "Hello world!"


@strawberry.type
class Query:  # pylint: disable=too-few-public-methods
    """Query"""

    message: str = strawberry.field(resolver=get_message)


schema = strawberry.Schema(query=Query)
