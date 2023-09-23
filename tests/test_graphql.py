"""Tests for Graphql query"""
import pytest

from flaskr import schema


@pytest.mark.asyncio
async def test_query():
    """Test graphql query"""
    query = """
      query {
        message
      }
    """

    result = await schema.schema.execute(query)
    assert result.data["message"] == "Hello world!"
