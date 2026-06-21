import requests
from my_logger import get_my_custom_logger

logger = get_my_custom_logger(__name__)

def api_call(method: str, url: str, **kwargs):
    logger.info(f"[REQUEST] => {method.upper()} {url}")
    if kwargs:
        logger.debug(f"Parametrs of request: (JSON/Headers): {kwargs}")

    response = requests.request(method, url, **kwargs)

    logger.info(f"📥 Ответ: Статус-код {response.status_code}")
    logger.debug(f"Тело ответа: {response.text}")

    return response