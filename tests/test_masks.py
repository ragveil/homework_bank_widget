import pytest

from src.masks import get_mask_account, get_mask_card_number

wrong_card = "Некорректный номер. Введите номер из 16 цифр без использования дополнительных символов."
wrong_account = "Некорректный номер. Введите номер из 20 цифр без использования дополнительных символов."


def test_get_mask_card_number_correct(card_number: str) -> None:
    """
    Тестируем функцию get_mask_card_number с использованием корректных данных.
    В данном тесте используется фикстура.
    :param card_number: Входные данные в виде строки.
    :return: Результат работы теста.
    """
    assert get_mask_card_number(card_number) == "5999 41** **** 6353"


@pytest.mark.parametrize(
    "card, expected",
    [
        ("", wrong_card),
        ("32148579", wrong_card),
        ("23409587340523451", wrong_card),
        ("5999 4142 2842 6353", wrong_card),
        ("5999-4142-2842-6353", wrong_card),
        ("номер карты", wrong_card),
        ("Карта 7809432185432148", wrong_card),
    ],
)
def test_get_mask_card_number_wrong(card: str, expected: str) -> None:
    """
    Тестируем функцию get_mask_card_number с использованием некорректных данных.
    В данном тесте используется параметризация.
    :param card: Входные данные в виде строки.
    :param expected: Ожидаемый результат.
    :return: Результат работы теста.
    """
    assert get_mask_card_number(card) == expected


def test_mask_account_correct(account_number: str) -> None:
    """
    Тестируем функцию get_mask_account с использованием корректных данных.
    В данном тесте используется фикстура.
    :param account_number: Входные данные в виде строки.
    :return: Результат работы теста.
    """
    assert get_mask_account(account_number) == "**4305"


@pytest.mark.parametrize(
    "account, expected",
    [
        ("", wrong_account),
        ("32148579", wrong_account),
        ("216323409587340523451", wrong_account),
        ("5999 4142 2842 6353", wrong_account),
        ("5999-4142-2842-6353", wrong_account),
        ("номер карты", wrong_account),
        ("Счет 78094321854321487493", wrong_account),
    ],
)
def test_mask_account_wrong(account: str, expected: str) -> None:
    """
    Тестируем функцию get_mask_account с использованием некорректных данных.
    В данном тесте используется параметризация.
    :param account: Входные данные в виде строки.
    :param expected: Ожидаемый результат.
    :return: Результат работы теста.
    """
    assert get_mask_account(account) == expected
