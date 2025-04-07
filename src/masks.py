def get_mask_card_number(card: str) -> str:
    """Принимает на вход номер карты в виде строки и возвращает замаскированное значение вида XXXX XX** **** XXXX"""
    return f"{card[0:4]} {card[4:6]}** **** {card[12:16]}"


def get_mask_account(account: str) -> str:
    """Принимает на вход номер счета в виде строки и возвращает замаскированное значение вида **XXXX"""
    return f"**{account[-4:]}"
