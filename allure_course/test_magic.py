import allure


@allure.title("Успешный тест (тут ничего не прикрепится)")
def test_success():
    assert 1 == 1


@allure.title("Упавший тест (здесь сработает магия из conftest.py)")
def test_fail_auto_attach():
    assert 2 + 2 == 4  # Вызываем падение теста
