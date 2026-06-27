# Импортируем нашу функцию из соседнего файла
from logger_config import get_logger

# Вызываем функцию и передаем ей __name__ (имя текущего файла)
logger = get_logger(__name__)


def test_user_can_login():
    logger.info("Открываем страницу логина")
    # ... тут код теста ...
