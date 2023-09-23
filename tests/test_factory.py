"""Test cases for test factory"""
from flaskr import create_app


def test_config():
    """Test factory configuration"""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing
