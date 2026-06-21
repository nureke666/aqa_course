def test_get_user_framework(api):
    # Действие (Act)
    response = api.get_user(1)

    # Проверка (Assert)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["firstName"] == "Emily"