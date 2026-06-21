import pytest
import requests

@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")
])
def test_users_names(user_id, expected_name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["name"] == expected_name