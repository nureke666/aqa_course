from my_logger import get_my_custom_logger

logger = get_my_custom_logger(__name__)
def test_cart_workflow():
    logger.debug("ID товара: 54321")
    logger.error("Ошибка: корзина пуста!")
    logger.info("Добавляем товар в корзину")
    logger.info("Переходим на страницу магазина")

    assert 1 == 0