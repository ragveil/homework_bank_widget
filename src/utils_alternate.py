import csv
import logging
import os
from typing import Any

import pandas

from config import ROOT_DIR

logs_path = os.path.join(ROOT_DIR, "logs", "utils_alternate.log")

operations_path = os.path.join(ROOT_DIR, "data\\")
csv_path = os.path.join(operations_path, "transactions.csv")
xls_path = os.path.join(operations_path, "transactions_excel.xlsx")

logger = logging.getLogger("utils_alternate")
file_handler = logging.FileHandler(logs_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_csv(path: str) -> Any:
    """
    Конвертирует данные из CSV-файла в объект Python со словарями о транзакциях.
    :param path: Входящее значение в виде пути до файла.
    :return: Результат работы функции, список.
    """
    logger.info(f"Начало работы функции {get_transactions_csv}")
    try:
        with open(path, encoding="UTF-8") as f:
            logger.info(f"CSV файл {path} успешно прочитан")
            operations_data = list(csv.DictReader(f, delimiter=";"))
            logger.info("Данные успешно обработаны из CSV")
    except (FileNotFoundError, csv.Error) as e:
        operations_data = []
        logger.error(f"В работе функции возникла ошибка {e}")
    return operations_data


def get_transactions_xls(path: str) -> Any:
    """
    Конвертирует данные из EXCEL-файла в объект Python со словарями о транзакциях.
    :param path: Входящее значение в виде пути до файла.
    :return: Результат работы функции, список.
    """
    logger.info(f"Начало работы функции {get_transactions_xls}")
    try:
        read_xls = pandas.read_excel(path)
        logger.info(f"Excel файл {path} успешно прочитан")
        operations_data = read_xls.to_dict(orient="records")
        logger.info("Данные успешно обработаны из excel")
    except (FileNotFoundError, UnicodeDecodeError) as e:
        operations_data = []
        logger.error(f"В работе функции возникла ошибка {e}")
    return operations_data
