import random
from string import digits

from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card


def bonus_generate_random(nums: str) -> str:
    """Бонусная функция.
    Принимает значения 'card' и 'account', генерирует номер карты или счета и возвращает в виде маски"""
    resp_num = "Некорректные данные"
    if nums == "card":
        generate_num = "".join(random.choices(digits, k=16))
        resp_num = get_mask_card_number(generate_num)
    elif nums == "account":
        generate_num = "".join(random.choices(digits, k=20))
        resp_num = get_mask_account(generate_num)
    return resp_num


print(bonus_generate_random("card"))
print(bonus_generate_random("account"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
