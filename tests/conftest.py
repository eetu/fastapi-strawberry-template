"""Module to bootstrap tests"""
from flask import Flask
import pytest
from flaskr import create_app


@pytest.fixture
def app():
    """Function to get test app"""
    test_app = create_app(
        {
            "TESTING": True,
        }
    )

    yield test_app


@pytest.fixture
def client(app: Flask):  # pylint: disable=redefined-outer-name
    """Function to get test client"""
    return app.test_client()
