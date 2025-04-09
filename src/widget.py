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
        return f"{both[:account.start()]} {get_mask_account(account.group())}"
    else:
        return ""


def get_date(date: str) -> str:
    """
    Форматирование даты и времени в корректный вид.

    :param date: Входящее значение в виде строки формата дата-время.
    :return: Строка со значением даты формата день.месяц.год
    """
    return datetime.fromisoformat(date).strftime("%d.%m.%Y")
