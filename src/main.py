import random
from string import digits
from typing import Any

from masks import get_mask_account, get_mask_card_number
from widget import get_date, mask_account_card

CARD_VARIANTS = ("Maestro", "MasterCard", "Visa Classic", "Visa", "Visa Platinum", "Visa Gold", "МИР")
TYPES_OF_NUMS = ("card", "account")


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
Счет: {get_mask_account('73654108430135874305')}"""
)
