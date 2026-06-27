import logging


def get_my_custom_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_handler = logging.FileHandler("framework.log")
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(filename)s] => %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
