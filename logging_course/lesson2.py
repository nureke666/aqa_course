import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] [%(levelname)s] [%(filename)s] => %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.info("Переходим на страницу магазина")
logging.debug("ID товара: 54321")
logging.info("Добавляем товар в корзину")
logging.error("Ошибка: корзина пуста!")
