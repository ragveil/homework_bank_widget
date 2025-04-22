import random
from string import digits
from typing import Any

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

CARD_VARIANTS = ("Maestro", "MasterCard", "Visa Classic", "Visa", "Visa Platinum", "Visa Gold", "МИР")
TYPES_OF_NUMS = ("card", "account")

banking_operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def bonus_generate_random(nums: str) -> str:
    """
    Бонусная функция для дополнительной проверки функции mask_account_card из модуля widget и наработка навыка автора.
    :param nums: Входящий тип запроса пользователя
    :return: Строка
    """
    if nums in TYPES_OF_NUMS:
        x: Any = lambda len_nums: "".join(random.choices(digits, k=len_nums))
        if nums == "card":
            return mask_account_card(f"{random.choice(CARD_VARIANTS)} {x(16)}")
        elif nums == "account":
            return mask_account_card(f"Счет {x(20)}")
    return "Некорректные данные"


print(
    f"""Проверка работы бонусной функции:
Карта: {bonus_generate_random("card")}
Счет: {bonus_generate_random("account")}""",
    end="\n\n",
)

print(
    f"""Проверка работоспособности функций модуля widget в рамках второй домашней работы:
Карта: {mask_account_card("Visa Gold 5999414228426353")}
Счет: {mask_account_card("Счет 73654108430135874305")}
Дата: {get_date("2024-03-11T02:26:18.671407")}""",
    end="\n\n",
)

print(
    f"""Проверки работоспособности функций модуля masks из первой домашней работы:
Карта: {get_mask_card_number('7000792289606361')}
Счет: {get_mask_account('73654108430135874305')}""",
    end="\n\n",
)

print(
    f"""Проверка работоспособности функций модуля processing в рамках третьей домашней работы:
Фильтрация по состоянию по умолчанию: {filter_by_state(banking_operations)}
Фильтрация по состоянию с использованием дополнительного аргумента: {filter_by_state(banking_operations, 'CANCELED')}
Сортировка даты по умолчанию: {sort_by_date(banking_operations)}
Сортировка даты с использованием дополнительного аргумента: {sort_by_date(banking_operations, False)}"""
)
