import pytest
import requests

url = "https://jsonplaceholder.typicode.com/users/2"

def test_get_user_info():
    response = requests.get(url)
    assert response.status_code == 200, "Ожидался код 200"
    data = response.json()
    assert data["name"] == "Ervin Howell", "Xz"
    assert "email" in data, "Ключ email отсутствует"