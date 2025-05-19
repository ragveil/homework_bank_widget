import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(both: str) -> str:
    """
    Маскирует данные банковских карт или счета.
    :param both: Входящее значение в виде строки с текстом и номером карты или счета.
    :return: Строка с использованием маски вида XXXX XX** **** XXXX или **ХХ.
    """
    if card := re.search(r"(\s\d{16}$)", both):
        return f"{both[:card.start()]} {get_mask_card_number(card.group()[1:])}"
    elif account := re.search(r"(\s\d{20}$)", both):
        return f"{both[:account.start()]} {get_mask_account(account.group()[1:])}"
    else:
        return "Некорректный номер."


def get_date(date: str) -> str:
    """
    Форматирование даты и времени в корректный вид.

    :param date: Входящее значение в виде строки формата дата-время.
    :return: Строка со значением даты формата день.месяц.год
    """
    if re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}", date):
        return datetime.fromisoformat(date).strftime("%d.%m.%Y")
    else:
        return "Некорректный формат даты."
