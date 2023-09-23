"""Test cases for API"""


def test_hello(client):
    """Tests hello endoint"""
    response = client.get("/hello")
    assert response.data == b"Hello, World!"
