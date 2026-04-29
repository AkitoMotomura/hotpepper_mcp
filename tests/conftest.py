import pytest
from app.client import HotpepperClient


@pytest.fixture
def client():
    return HotpepperClient(api_key="test_key")
