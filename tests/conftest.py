import pytest
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def client():
    client = TestClient(app=app)

    return client
