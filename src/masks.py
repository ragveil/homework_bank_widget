import logging
import os
import re

from config import ROOT_DIR

logs_path = os.path.join(ROOT_DIR, "logs", "masks.log")

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(logs_path, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card: str) -> str:
    """
    Маскирует номер банковской карты.
    :param card: Входящее значение в виде строки с номером карты.
    :return: Строка с использованием маски вида XXXX XX** **** XXXX
    """
    logger.info(f"Начало работы функции {get_mask_card_number}")
    if re.match(r"\d{16}$", card):
        logger.info("Успешное применение маски к номеру карты")
        return f"{card[0:4]} {card[4:6]}** **** {card[12:16]}"
    else:
        logger.error(f"Ошибка {ValueError}: Неверные данные для обработки")
        return "Некорректный номер. Введите номер из 16 цифр без использования дополнительных символов."


def get_mask_account(account: str) -> str:
    """
    Маскирует номер счета.

    :param account: Входящее значение в виде строки с номером счета.
    :return: Строка с использованием маски вида **XXXX
    """
    logger.info(f"Начало работы функции {get_mask_account}")
    if re.match(r"\d{20}$", account):
        logger.info("Успешное применение маски к номеру счета")
        return f"**{account[-4:]}"
    else:
        logger.error(f"Ошибка {ValueError}: Неверные данные для обработки")
        return "Некорректный номер. Введите номер из 20 цифр без использования дополнительных символов."
