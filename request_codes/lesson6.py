import requests

URL = 'https://jsonplaceholder.typicode.com/posts/1'


def test_update_post():
    payload = {
        "id": 1,
        "title": "New title",
        "body": "New text",
        "userId": 1,
    }
    response = requests.put(URL, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "New title"


def test_delete_post():
    response = requests.delete(URL)
    assert response.status_code in (200, 204), f"Неожиданный код: {response.status_code}"

    data = response.json()
    assert data == {}