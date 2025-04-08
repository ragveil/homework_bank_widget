import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(both: str) -> str:
    """Принимает значение карты или счета в виде строки и возвращает замаскированное значение вида:
    Тип карты ХХХХ ХХ** **** ХХХХ
    Счет **ХХ"""
    if card := re.search(r"(\s\d{16}$)", both):
        return f"{both[:card.start()]} {get_mask_card_number(card.group()[1:])}"
    elif account := re.search(r"(\s\d{20}$)", both):
        return f"{both[:account.start()]} {get_mask_account(account.group())}"
    else:
        return ""


def get_date(date: str) -> str:
    """Принимает значение даты и времени в виде строки и возвращает корректную дату"""
    return datetime.fromisoformat(date).strftime("%d.%m.%Y")
