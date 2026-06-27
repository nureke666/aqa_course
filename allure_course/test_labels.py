import allure


@allure.epic("Авторизация")
# Ставим максимальный приоритет
@allure.severity(allure.severity_level.BLOCKER)
# Прикрепляем ссылку на баг
@allure.issue("AUTH-123", "Баг: Ошибка 500 при логине")
# Прикрепляем ссылку на документацию
@allure.link(
    "https://ru.wikipedia.org/wiki/Система_отслеживания_ошибок", name="Документация"
)
@allure.title("Проверка успешного логина (Критичный функционал)")
def test_login_success():
    with allure.step("Вводим правильный логин и пароль"):
        pass
    with allure.step("Проверяем успешный вход"):
        assert True


@allure.epic("UI Дизайн")
# Ставим минимальный приоритет
@allure.severity(allure.severity_level.MINOR)
@allure.title("Проверка опечатки в футере (Минорный функционал)")
def test_footer_text():
    with allure.step("Скроллим страницу вниз"):
        pass
    with allure.step("Проверяем текст в футере"):
        assert True
