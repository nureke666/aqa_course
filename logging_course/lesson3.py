import logging

logger = logging.getLogger("API_TESTS")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("test_run.log")

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(filename)s] => %(message)s")

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Переходим на страницу магазина")
logger.debug("ID товара: 54321")
logger.info("Добавляем товар в корзину")
logger.error("Ошибка: корзина пуста!")
