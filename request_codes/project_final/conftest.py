import pytest
from api_client import APIClient

@pytest.fixture
def api():
    # Эта фикстура будет инициализировать наш класс перед каждым тестом
    return APIClient()