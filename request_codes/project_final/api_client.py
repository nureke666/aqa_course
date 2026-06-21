import requests

class APIClient:
    def __init__(self):
        # Базовый URL хранится в одном месте!
        self.base_url = "https://dummyjson.com"
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    # Метод для получения пользователя
    def get_user(self, user_id):
        # Клиент сам склеивает базовый URL и эндпоинт
        response = self.session.get(f"{self.base_url}/users/{user_id}")
        return response