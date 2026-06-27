import logging

# Базовая настройка
logging.basicConfig(level=logging.DEBUG)

logging.debug("Это DEBUG сообщение (оно спрятано)")
logging.info("Это INFO сообщение (нормальный ход работы)")
logging.warning("Это WARNING сообщение (внимание!)")
logging.error("Это ERROR сообщение (ошибка!)")
logging.critical("Это CRITICAL сообщение (всё сломалось!)")
