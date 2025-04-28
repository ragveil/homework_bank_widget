import pytest

from src.widget import get_date, mask_account_card

wrong_account_card = "Некорректный номер."
wrong_date = "Некорректный формат даты."


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Карта вашего банка 1234567890123456", "Карта вашего банка 1234 56** **** 3456"),
        ("Счёт 35383033474447895560", "Счёт **5560"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask_account_card_correct(number: str, expected: str) -> None:
    """
    Тестируем функцию mask_account_card с использованием разных счетов и карт различных платежных систем.
    В данном тесте используется параметризация.
    :param number: Входные данные в виде строки.
    :param expected: Ожидаемый результат.
    :return: Результат работы теста.
    """
    assert mask_account_card(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        ("", wrong_account_card),
        ("Карта 324509853", wrong_account_card),
        ("Счет 1235126", wrong_account_card),
        ("73654108430135874305", wrong_account_card),
        ("5999414228426353", wrong_account_card),
        ("какие-нибудь символы", wrong_account_card),
        ("Visa Gold 5999 4142 2842 6353", wrong_account_card),
        ("Счет 7365 4108 4301 3587 4305", wrong_account_card),
    ],
)
def test_mask_account_card_wrong(number: str, expected: str) -> None:
    """
    Тестируем функцию mask_account_card с использованием некорректных данных.
    В данном тесте используется параметризация.
    :param number: Входные данные в виде строки.
    :param expected: Ожидаемый результат.
    :return: Результат работы теста.
    """
    assert mask_account_card(number) == expected


def test_get_date_correct(date: str) -> None:
    """
    Тестируем функцию get_date с использованием корректных данных.
    В данном тесте используется фикстура.
    :param date: Входные данные в виде строки.
    :return: Результат работы теста.
    """
    assert get_date(date) == "11.03.2024"


@pytest.mark.parametrize(
    "date, expected",
    [
        ("", wrong_date),
        ("11.03.2024", wrong_date),
        ("2024-03-1102:26:18.671407", wrong_date),
        ("2024.03.11T02:26:18.671407", wrong_date),
        ("2024-3-11T2:26:18.671407", wrong_date),
    ],
)
def test_get_date_wrong(date: str, expected: str) -> None:
    """
    Тестируем функцию get_date с использованием некорректных данных.
    В данном тесте используется параметризация.
    :param date: Входные данные в виде строки.
    :param expected: Ожидаемый результат.
    :return: Результат работы теста.
    """
    assert get_date(date) == expected
