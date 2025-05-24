import json
import logging
import os
from typing import Any

from config import ROOT_DIR

logs_path = os.path.join(ROOT_DIR, "logs", "utils.log")

operations_path = os.path.join(ROOT_DIR, "data\\")

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(logs_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions(path: str) -> Any:
    """
    Конвертирует данные из JSON-файла в объект Python со словарями о транзакциях.
    :param path: Входящее значение в виде пути до файла.
    :return: Результат работы функции, список.
    """
    logger.info(f"Начало работы функции {get_transactions}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            logger.info(f"Файл {path} успешно прочитан")
            operations_data = json.load(f)
            logger.info("Данные успешно обработаны")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        operations_data = []
        logger.error(f"В работе функции возникла ошибка {e}")
    return operations_data
