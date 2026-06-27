import allure


# Способ 2: Декоратор над функцией (с подстановкой переменных)
@allure.step("Подготовка пользователя: {user_id} с ролью {role}")
def prepare_user(user_id, role):
    # Имитируем создание юзера в БД
    print(f"Создаем юзера {user_id} в базе")
    return True


@allure.step("Отправка API запроса на покупку товара {item_name}")
def buy_item(item_name):
    # Имитируем логику покупки
    if item_name == "Сломанный_товар":
        # Специально вызываем ошибку (исключение), чтобы сломать шаг
        raise ValueError("Сервер ответил ошибкой 500!")
    return "success"


# Сам тест
@allure.title("Проверка покупки товара")
def test_buy_standard_item():
    # Способ 1: Использование with (контекстного менеджера)
    with allure.step("Шаг 1: Инициализация системы"):
        print("Система запущена")
        assert 1 == 1

    # Вызываем функции-шаги
    prepare_user(user_id=105, role="VIP")

    with allure.step("Шаг 3: Совершаем покупку и проверяем результат"):
        result = buy_item(item_name="Ноутбук")
        assert result == "success"


@allure.title("Покупка проблемного товара (тест упадет)")
def test_buy_broken_item():
    prepare_user(user_id=999, role="Standard")
    # Передаем товар, который вызовет ошибку внутри шага
    buy_item(item_name="Сломанный_товар")
