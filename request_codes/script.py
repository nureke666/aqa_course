import requests

def test_create_album_success():
    # 1. Arrange (Подготовка) & Act (Действие)
    url = "https://jsonplaceholder.typicode.com/albums"
    payload = {"title": "Test Album", "userId": 1}
    response = requests.post(url, json=payload)
    
    # 2. Assert (Проверки)
    assert response.status_code == 201, "Неверный статус-код"
    
    # Можно проверять и само тело ответа!
    data = response.json()
    assert data["title"] == "Test Album", "Название альбома сохранилось неверно"
    assert "id" in data, "Сервер не присвоил ID новому альбому"