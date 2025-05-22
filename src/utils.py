import json
import os
from typing import Any

from config import ROOT_DIR

operations_path = os.path.join(ROOT_DIR, "data\\")


def get_transactions(path: str) -> Any:
    """
    Конвертирует данные из JSON-файла в объект Python со словарями о транзакциях.
    :param path: Входящее значение в виде пути до файла.
    :return: Результат работы функции, список.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            operations_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        operations_data = []
    return operations_data
