import requests


def test_user_not_found():
    url = "https://jsonplaceholder.typicode.com/users/9999"
    response = requests.get(url)
    assert response.status_code == 404, (
        "Ожидался код 404 для несуществующего пользователя"
    )


def test_custom_headerss():
    url = "https://httpbin.org/headers"
    headers_dict = {"Secret-Token": "aqa_junior_123"}
    response = requests.get(url, headers=headers_dict)
    assert response.status_code == 200, "Ожидался код 200"
    data = response.json()
    assert data["headers"]["Secret-Token"] == "aqa_junior_123", (
        "Заголовок Secret-Token не был отправлен или сохранён неверно"
    )
