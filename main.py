import random
from string import digits

from src.masks import get_mask_account, get_mask_card_number


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
