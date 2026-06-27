import requests
import pytest


@pytest.fixture()
def api_client():
    session = requests.Session()
    session.headers.update({"User-Agent": "My-AQA-Bot/1.0"})
    return session


def test_check_user_agent(api_client):
    response = api_client.get("https://postman-echo.com/get", timeout=5)
    assert response.status_code == 200

    data = response.json()
    assert data["headers"]["user-agent"] == "My-AQA-Bot/1.0"
