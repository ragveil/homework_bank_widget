def get_mask_card_number(card: str) -> str:
    """
    Маскирует номер банковской карты.

    :param card: Входящее значение в виде строки с номером карты.
    :return: Строка с использованием маски вида XXXX XX** **** XXXX
    """
    return f"{card[0:4]} {card[4:6]}** **** {card[12:16]}"


def get_mask_account(account: str) -> str:
    """
    Маскирует номер счета.

    :param account: Входящее значение в виде строки с номером счета.
    :return: Строка с использованием маски вида **XXXX
    """

    return f"**{account[-4:]}"
