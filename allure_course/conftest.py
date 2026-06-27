import pytest
import allure


# Этот хук вызывается pytest'ом после выполнения каждого этапа теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Выполняем все остальные хуки до получения репорта (внутренняя кухня pytest)
    outcome = yield
    rep = outcome.get_result()

    # Проверяем, что тест именно УПАЛ (failed) и именно на этапе ВЫПОЛНЕНИЯ (call), а не при сетапе
    if rep.when == "call" and rep.failed:
        # МАГИЯ НАЧИНАЕТСЯ ЗДЕСЬ
        # В реальном UI-проекте здесь ты попросишь вебдрайвер сделать скриншот:
        # screenshot = driver.get_screenshot_as_png()

        # А мы для примера просто прикрепим авто-сообщение
        error_text = (
            f"Тест '{item.name}' упал! Это автоматическое вложение из conftest.py"
        )

        allure.attach(
            body=error_text,
            name="АВТОМАТИЧЕСКИЙ ЛОГ ОШИБКИ",
            attachment_type=allure.attachment_type.TEXT,  # Для скриншота тут был бы PNG
        )
