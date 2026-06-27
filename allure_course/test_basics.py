def test_success():
    """Этот тест должен пройти успешно"""
    assert 10 == 10


def test_failure():
    """Этот тест специально упадет"""
    assert 2 + 2 == 5


def test_skip():
    """Этот тест мы пропустим"""
    import pytest

    pytest.skip("Пропускаем тест для демонстрации Allure")
