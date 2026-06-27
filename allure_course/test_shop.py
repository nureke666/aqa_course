import allure


@allure.epic("Интернет-магазин")
@allure.feature("Корзина")
class TestCart:
    @allure.story("Успешное добавление товара")
    @allure.title("Добавление товара авторизованным пользователем")
    @allure.description(
        "Проверяем, что товар появляется в корзине, если юзер залогинен"
    )
    def test_add_item_logged_in(self):
        # Имитируем успешный тест
        assert True

    @allure.story("Ошибка добавления товара")
    @allure.title("Попытка добавления товара анонимом")
    @allure.description("Система должна выдать ошибку 401, если юзер не залогинен")
    def test_add_item_anonymous(self):
        # Имитируем упавший тест (представим, что бага)
        assert 401 == 200


@allure.epic("Интернет-магазин")
@allure.feature("Оплата")
class TestCheckout:
    @allure.story("Оплата картой")
    @allure.title("Успешная оплата привязанной картой")
    def test_payment_success(self):
        assert True
