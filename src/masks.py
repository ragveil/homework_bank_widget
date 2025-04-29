import re


def get_mask_card_number(card: str) -> str:
    """
    Маскирует номер банковской карты.

    :param card: Входящее значение в виде строки с номером карты.
    :return: Строка с использованием маски вида XXXX XX** **** XXXX
    """
    if re.match(r"\d{16}$", card):
        return f"{card[0:4]} {card[4:6]}** **** {card[12:16]}"
    else:
        return "Некорректный номер. Введите номер из 16 цифр без использования дополнительных символов."


def get_mask_account(account: str) -> str:
    """
    Маскирует номер счета.

    :param account: Входящее значение в виде строки с номером счета.
    :return: Строка с использованием маски вида **XXXX
    """
    if re.match(r"\d{20}$", account):
        return f"**{account[-4:]}"
    else:
        return "Некорректный номер. Введите номер из 20 цифр без использования дополнительных символов."
