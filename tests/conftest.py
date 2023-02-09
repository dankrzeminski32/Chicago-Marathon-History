import pytest
from src.backend import init_app
from backend.config import TestConfig


@pytest.fixture(scope="module")
def test_client():
    flask_app = init_app(TestConfig)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!
