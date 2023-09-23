"""GraphQL Schema"""
import strawberry


def get_message() -> str:
    """Get message function"""
    return "Hello world!"


@strawberry.type
class Query:
    """Query"""

    message: str = strawberry.field(resolver=get_message)


schema = strawberry.Schema(query=Query)
