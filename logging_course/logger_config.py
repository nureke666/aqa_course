import logging


def get_logger(name):
    # Создаем логгера с тем именем, которое нам передадут
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Чтобы логи не дублировались, если мы вызовем функцию дважды, проверяем:
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        # Можно добавить и FileHandler сюда же...

        formatter = logging.Formatter("[%(name)s] => %(message)s")
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger
