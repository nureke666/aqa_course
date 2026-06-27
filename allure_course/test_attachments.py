import allure
import json


@allure.epic("API Тесты")
@allure.feature("Пользователи")
class TestUsersAPI:
    @allure.title("Проверка создания пользователя и прикрепление ответа (JSON)")
    def test_create_user_attach_json(self):
        with allure.step("Шаг 1: Формируем тело запроса (Request)"):
            request_payload = {"name": "Nurik", "job": "AQA Engineer"}
            # Прикрепляем то, что мы якобы отправляем
            allure.attach(
                body=json.dumps(
                    request_payload, indent=4
                ),  # превращаем dict в красивую строку JSON
                name="Request Payload",
                attachment_type=allure.attachment_type.JSON,
            )

        with allure.step("Шаг 2: Получаем ответ от сервера (Response)"):
            # Имитируем ответ сервера (как будто мы использовали библиотеку requests)
            response_data = {
                "id": 777,
                "name": "Nurik",
                "job": "AQA Engineer",
                "createdAt": "2026-06-22T00:00:00Z",
            }

            # Прикрепляем ответ сервера
            allure.attach(
                body=json.dumps(response_data, indent=4),
                name="Server Response",
                attachment_type=allure.attachment_type.JSON,
            )

        with allure.step("Шаг 3: Проверяем данные"):
            assert response_data["id"] == 777
            assert response_data["name"] == "Nurik"

    @allure.title("Проверка логов (Text)")
    def test_attach_plain_text(self):
        with allure.step("Прикрепляем текстовый лог"):
            log_text = "ERROR 2026-06-22: Database connection timeout\nTraceback: ..."
            allure.attach(
                body=log_text,
                name="Server Logs",
                attachment_type=allure.attachment_type.TEXT,
            )
