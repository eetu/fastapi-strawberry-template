"""Tests for Graphql query"""
import pytest

from . import graphql


@pytest.mark.asyncio
async def test_query():
    """Test graphql query"""
    query = """
      query {
        message
      }
    """

    result = await graphql.schema.execute(query)
    assert result.data["message"] == "Hello world!"
